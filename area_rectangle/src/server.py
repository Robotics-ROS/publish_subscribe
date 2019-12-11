#!/usr/bin/python
import rospy
from area_rectangle.srv import area, areaRequest, areaResponse
def areaCal(req):
    rospy.loginfo('length {}, width {}'.format(req.length, req.width))
    rospy.loginfo('area {:.2f}'.format(req.length * req.width))
    return areaResponse(req.length * req.width)



# if __name__ == "__main__":
print('init')
rospy.init_node('server_node', anonymous=True)
s= rospy.Service('areaCal', area, areaCal)
print(s.resolved_name)
rospy.spin()
