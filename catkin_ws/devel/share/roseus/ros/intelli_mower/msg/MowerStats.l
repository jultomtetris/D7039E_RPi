;; Auto-generated. Do not edit!


(when (boundp 'intelli_mower::MowerStats)
  (if (not (find-package "INTELLI_MOWER"))
    (make-package "INTELLI_MOWER"))
  (shadow 'MowerStats (find-package "INTELLI_MOWER")))
(unless (find-package "INTELLI_MOWER::MOWERSTATS")
  (make-package "INTELLI_MOWER::MOWERSTATS"))

(in-package "ROS")
;;//! \htmlinclude MowerStats.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass intelli_mower::MowerStats
  :super ros::object
  :slots (_header _command _bumperFront _bumperBack _emergency _cutter _lift _leftSpeed _rightSpeed _outerRight _innerRight _innerLeft _outerLeft _xPos _yPos _heading ))

(defmethod intelli_mower::MowerStats
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:command __command) "")
    ((:bumperFront __bumperFront) "")
    ((:bumperBack __bumperBack) "")
    ((:emergency __emergency) "")
    ((:cutter __cutter) "")
    ((:lift __lift) "")
    ((:leftSpeed __leftSpeed) 0.0)
    ((:rightSpeed __rightSpeed) 0.0)
    ((:outerRight __outerRight) 0.0)
    ((:innerRight __innerRight) 0.0)
    ((:innerLeft __innerLeft) 0.0)
    ((:outerLeft __outerLeft) 0.0)
    ((:xPos __xPos) 0.0)
    ((:yPos __yPos) 0.0)
    ((:heading __heading) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _command (string __command))
   (setq _bumperFront (string __bumperFront))
   (setq _bumperBack (string __bumperBack))
   (setq _emergency (string __emergency))
   (setq _cutter (string __cutter))
   (setq _lift (string __lift))
   (setq _leftSpeed (float __leftSpeed))
   (setq _rightSpeed (float __rightSpeed))
   (setq _outerRight (float __outerRight))
   (setq _innerRight (float __innerRight))
   (setq _innerLeft (float __innerLeft))
   (setq _outerLeft (float __outerLeft))
   (setq _xPos (float __xPos))
   (setq _yPos (float __yPos))
   (setq _heading (float __heading))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:command
   (&optional __command)
   (if __command (setq _command __command)) _command)
  (:bumperFront
   (&optional __bumperFront)
   (if __bumperFront (setq _bumperFront __bumperFront)) _bumperFront)
  (:bumperBack
   (&optional __bumperBack)
   (if __bumperBack (setq _bumperBack __bumperBack)) _bumperBack)
  (:emergency
   (&optional __emergency)
   (if __emergency (setq _emergency __emergency)) _emergency)
  (:cutter
   (&optional __cutter)
   (if __cutter (setq _cutter __cutter)) _cutter)
  (:lift
   (&optional __lift)
   (if __lift (setq _lift __lift)) _lift)
  (:leftSpeed
   (&optional __leftSpeed)
   (if __leftSpeed (setq _leftSpeed __leftSpeed)) _leftSpeed)
  (:rightSpeed
   (&optional __rightSpeed)
   (if __rightSpeed (setq _rightSpeed __rightSpeed)) _rightSpeed)
  (:outerRight
   (&optional __outerRight)
   (if __outerRight (setq _outerRight __outerRight)) _outerRight)
  (:innerRight
   (&optional __innerRight)
   (if __innerRight (setq _innerRight __innerRight)) _innerRight)
  (:innerLeft
   (&optional __innerLeft)
   (if __innerLeft (setq _innerLeft __innerLeft)) _innerLeft)
  (:outerLeft
   (&optional __outerLeft)
   (if __outerLeft (setq _outerLeft __outerLeft)) _outerLeft)
  (:xPos
   (&optional __xPos)
   (if __xPos (setq _xPos __xPos)) _xPos)
  (:yPos
   (&optional __yPos)
   (if __yPos (setq _yPos __yPos)) _yPos)
  (:heading
   (&optional __heading)
   (if __heading (setq _heading __heading)) _heading)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; string _command
    4 (length _command)
    ;; string _bumperFront
    4 (length _bumperFront)
    ;; string _bumperBack
    4 (length _bumperBack)
    ;; string _emergency
    4 (length _emergency)
    ;; string _cutter
    4 (length _cutter)
    ;; string _lift
    4 (length _lift)
    ;; float64 _leftSpeed
    8
    ;; float64 _rightSpeed
    8
    ;; float64 _outerRight
    8
    ;; float64 _innerRight
    8
    ;; float64 _innerLeft
    8
    ;; float64 _outerLeft
    8
    ;; float64 _xPos
    8
    ;; float64 _yPos
    8
    ;; float64 _heading
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; string _command
       (write-long (length _command) s) (princ _command s)
     ;; string _bumperFront
       (write-long (length _bumperFront) s) (princ _bumperFront s)
     ;; string _bumperBack
       (write-long (length _bumperBack) s) (princ _bumperBack s)
     ;; string _emergency
       (write-long (length _emergency) s) (princ _emergency s)
     ;; string _cutter
       (write-long (length _cutter) s) (princ _cutter s)
     ;; string _lift
       (write-long (length _lift) s) (princ _lift s)
     ;; float64 _leftSpeed
       (sys::poke _leftSpeed (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _rightSpeed
       (sys::poke _rightSpeed (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _outerRight
       (sys::poke _outerRight (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _innerRight
       (sys::poke _innerRight (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _innerLeft
       (sys::poke _innerLeft (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _outerLeft
       (sys::poke _outerLeft (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _xPos
       (sys::poke _xPos (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _yPos
       (sys::poke _yPos (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _heading
       (sys::poke _heading (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; string _command
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _command (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _bumperFront
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _bumperFront (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _bumperBack
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _bumperBack (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _emergency
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _emergency (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _cutter
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _cutter (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _lift
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _lift (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float64 _leftSpeed
     (setq _leftSpeed (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _rightSpeed
     (setq _rightSpeed (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _outerRight
     (setq _outerRight (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _innerRight
     (setq _innerRight (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _innerLeft
     (setq _innerLeft (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _outerLeft
     (setq _outerLeft (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _xPos
     (setq _xPos (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _yPos
     (setq _yPos (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _heading
     (setq _heading (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get intelli_mower::MowerStats :md5sum-) "279c6ecbaca551e207950878b3b76dbd")
(setf (get intelli_mower::MowerStats :datatype-) "intelli_mower/MowerStats")
(setf (get intelli_mower::MowerStats :definition-)
      "Header header
string command
string bumperFront
string bumperBack
string emergency
string cutter
string lift
float64 leftSpeed
float64 rightSpeed
float64 outerRight
float64 innerRight
float64 innerLeft
float64 outerLeft
float64 xPos
float64 yPos
float64 heading

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

")



(provide :intelli_mower/MowerStats "279c6ecbaca551e207950878b3b76dbd")


