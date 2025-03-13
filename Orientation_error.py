#ORIENTATION ERROR

#The unit quaternions are defined as q = np.array([x, y, z, w])

#Compute the Skew-Symm. matrix for the desired orientation
skew_des = np.array([[int(0), -actual_target_quat[2], actual_target_quat[1]], [actual_target_quat[2], int(0) , -actual_target_quat[0]], [-actual_target_quat[1], actual_target_quat[0], int(0)]])
#Compute the orientation error
orientation_err = (actual_quat[3]*np.array([actual_target_quat[0], actual_target_quat[1], actual_target_quat[2]])) - (actual_target_quat[3]*np.array([actual_quat[0], actual_quat[1], actual_quat[2]])) - np.matmul(skew_des,np.array([actual_quat[0], actual_quat[1], actual_quat[2]])) 
