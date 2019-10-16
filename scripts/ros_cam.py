#!/usr/bin/env python

import rospy

def hello():
    rospy.init_node('hello', anonymous=True)
    rospy.loginfo("Hello World")


if __name__ == '__main__':
    hello()
