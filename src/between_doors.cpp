
#include "bwi_kr_execution/ExecutePlanAction.h"

#include <actionlib/client/simple_action_client.h>

#include <ros/ros.h>

typedef actionlib::SimpleActionClient<bwi_kr_execution::ExecutePlanAction> Client;

using namespace std;

int main(int argc, char**argv) {
  ros::init(argc, argv, "between_doors");
  ros::NodeHandle n;

  ros::NodeHandle privateNode("~");
  string locationA;
  privateNode.param<string>("a",locationA,"d3_414b1");

  string locationB;
  privateNode.param<string>("b",locationB,"d3_414b2");



  Client client("/action_executor/execute_plan", true);
  client.waitForServer();

  bool fromAtoB = true;

  while (ros::ok()) {

    string location = (fromAtoB)? locationB : locationA;

    fromAtoB = !fromAtoB;

    ROS_INFO_STREAM("going to " << location);

    bwi_kr_execution::ExecutePlanGoal goal;

    bwi_kr_execution::AspRule rule;
    bwi_kr_execution::AspFluent fluent;
    fluent.name = "not facing";

    fluent.variables.push_back(location);

    rule.body.push_back(fluent);
    goal.aspGoal.push_back(rule);

    ROS_INFO("sending goal");
    client.sendGoalAndWait(goal);

    if (client.getState() == actionlib::SimpleClientGoalState::ABORTED) {
      ROS_INFO("Aborted");
    } else if (client.getState() == actionlib::SimpleClientGoalState::PREEMPTED) {
      ROS_INFO("Preempted");
    }

    else if (client.getState() == actionlib::SimpleClientGoalState::SUCCEEDED) {
      ROS_INFO("Succeeded!");
    } else
      ROS_INFO("Terminated");

  }

  return 0;
}