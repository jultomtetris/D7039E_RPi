// Auto-generated. Do not edit!

// (in-package intelli_mower.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class MowerStats {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.command = null;
      this.bumperFront = null;
      this.bumperBack = null;
      this.emergency = null;
      this.cutter = null;
      this.lift = null;
      this.leftSpeed = null;
      this.rightSpeed = null;
      this.outerRight = null;
      this.innerRight = null;
      this.innerLeft = null;
      this.outerLeft = null;
      this.xPos = null;
      this.yPos = null;
      this.heading = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('command')) {
        this.command = initObj.command
      }
      else {
        this.command = '';
      }
      if (initObj.hasOwnProperty('bumperFront')) {
        this.bumperFront = initObj.bumperFront
      }
      else {
        this.bumperFront = '';
      }
      if (initObj.hasOwnProperty('bumperBack')) {
        this.bumperBack = initObj.bumperBack
      }
      else {
        this.bumperBack = '';
      }
      if (initObj.hasOwnProperty('emergency')) {
        this.emergency = initObj.emergency
      }
      else {
        this.emergency = '';
      }
      if (initObj.hasOwnProperty('cutter')) {
        this.cutter = initObj.cutter
      }
      else {
        this.cutter = '';
      }
      if (initObj.hasOwnProperty('lift')) {
        this.lift = initObj.lift
      }
      else {
        this.lift = '';
      }
      if (initObj.hasOwnProperty('leftSpeed')) {
        this.leftSpeed = initObj.leftSpeed
      }
      else {
        this.leftSpeed = 0.0;
      }
      if (initObj.hasOwnProperty('rightSpeed')) {
        this.rightSpeed = initObj.rightSpeed
      }
      else {
        this.rightSpeed = 0.0;
      }
      if (initObj.hasOwnProperty('outerRight')) {
        this.outerRight = initObj.outerRight
      }
      else {
        this.outerRight = 0.0;
      }
      if (initObj.hasOwnProperty('innerRight')) {
        this.innerRight = initObj.innerRight
      }
      else {
        this.innerRight = 0.0;
      }
      if (initObj.hasOwnProperty('innerLeft')) {
        this.innerLeft = initObj.innerLeft
      }
      else {
        this.innerLeft = 0.0;
      }
      if (initObj.hasOwnProperty('outerLeft')) {
        this.outerLeft = initObj.outerLeft
      }
      else {
        this.outerLeft = 0.0;
      }
      if (initObj.hasOwnProperty('xPos')) {
        this.xPos = initObj.xPos
      }
      else {
        this.xPos = 0.0;
      }
      if (initObj.hasOwnProperty('yPos')) {
        this.yPos = initObj.yPos
      }
      else {
        this.yPos = 0.0;
      }
      if (initObj.hasOwnProperty('heading')) {
        this.heading = initObj.heading
      }
      else {
        this.heading = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MowerStats
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [command]
    bufferOffset = _serializer.string(obj.command, buffer, bufferOffset);
    // Serialize message field [bumperFront]
    bufferOffset = _serializer.string(obj.bumperFront, buffer, bufferOffset);
    // Serialize message field [bumperBack]
    bufferOffset = _serializer.string(obj.bumperBack, buffer, bufferOffset);
    // Serialize message field [emergency]
    bufferOffset = _serializer.string(obj.emergency, buffer, bufferOffset);
    // Serialize message field [cutter]
    bufferOffset = _serializer.string(obj.cutter, buffer, bufferOffset);
    // Serialize message field [lift]
    bufferOffset = _serializer.string(obj.lift, buffer, bufferOffset);
    // Serialize message field [leftSpeed]
    bufferOffset = _serializer.float64(obj.leftSpeed, buffer, bufferOffset);
    // Serialize message field [rightSpeed]
    bufferOffset = _serializer.float64(obj.rightSpeed, buffer, bufferOffset);
    // Serialize message field [outerRight]
    bufferOffset = _serializer.float64(obj.outerRight, buffer, bufferOffset);
    // Serialize message field [innerRight]
    bufferOffset = _serializer.float64(obj.innerRight, buffer, bufferOffset);
    // Serialize message field [innerLeft]
    bufferOffset = _serializer.float64(obj.innerLeft, buffer, bufferOffset);
    // Serialize message field [outerLeft]
    bufferOffset = _serializer.float64(obj.outerLeft, buffer, bufferOffset);
    // Serialize message field [xPos]
    bufferOffset = _serializer.float64(obj.xPos, buffer, bufferOffset);
    // Serialize message field [yPos]
    bufferOffset = _serializer.float64(obj.yPos, buffer, bufferOffset);
    // Serialize message field [heading]
    bufferOffset = _serializer.float64(obj.heading, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MowerStats
    let len;
    let data = new MowerStats(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [command]
    data.command = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [bumperFront]
    data.bumperFront = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [bumperBack]
    data.bumperBack = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [emergency]
    data.emergency = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [cutter]
    data.cutter = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [lift]
    data.lift = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [leftSpeed]
    data.leftSpeed = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [rightSpeed]
    data.rightSpeed = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [outerRight]
    data.outerRight = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [innerRight]
    data.innerRight = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [innerLeft]
    data.innerLeft = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [outerLeft]
    data.outerLeft = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [xPos]
    data.xPos = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [yPos]
    data.yPos = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [heading]
    data.heading = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    length += object.command.length;
    length += object.bumperFront.length;
    length += object.bumperBack.length;
    length += object.emergency.length;
    length += object.cutter.length;
    length += object.lift.length;
    return length + 96;
  }

  static datatype() {
    // Returns string type for a message object
    return 'intelli_mower/MowerStats';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '279c6ecbaca551e207950878b3b76dbd';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MowerStats(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.command !== undefined) {
      resolved.command = msg.command;
    }
    else {
      resolved.command = ''
    }

    if (msg.bumperFront !== undefined) {
      resolved.bumperFront = msg.bumperFront;
    }
    else {
      resolved.bumperFront = ''
    }

    if (msg.bumperBack !== undefined) {
      resolved.bumperBack = msg.bumperBack;
    }
    else {
      resolved.bumperBack = ''
    }

    if (msg.emergency !== undefined) {
      resolved.emergency = msg.emergency;
    }
    else {
      resolved.emergency = ''
    }

    if (msg.cutter !== undefined) {
      resolved.cutter = msg.cutter;
    }
    else {
      resolved.cutter = ''
    }

    if (msg.lift !== undefined) {
      resolved.lift = msg.lift;
    }
    else {
      resolved.lift = ''
    }

    if (msg.leftSpeed !== undefined) {
      resolved.leftSpeed = msg.leftSpeed;
    }
    else {
      resolved.leftSpeed = 0.0
    }

    if (msg.rightSpeed !== undefined) {
      resolved.rightSpeed = msg.rightSpeed;
    }
    else {
      resolved.rightSpeed = 0.0
    }

    if (msg.outerRight !== undefined) {
      resolved.outerRight = msg.outerRight;
    }
    else {
      resolved.outerRight = 0.0
    }

    if (msg.innerRight !== undefined) {
      resolved.innerRight = msg.innerRight;
    }
    else {
      resolved.innerRight = 0.0
    }

    if (msg.innerLeft !== undefined) {
      resolved.innerLeft = msg.innerLeft;
    }
    else {
      resolved.innerLeft = 0.0
    }

    if (msg.outerLeft !== undefined) {
      resolved.outerLeft = msg.outerLeft;
    }
    else {
      resolved.outerLeft = 0.0
    }

    if (msg.xPos !== undefined) {
      resolved.xPos = msg.xPos;
    }
    else {
      resolved.xPos = 0.0
    }

    if (msg.yPos !== undefined) {
      resolved.yPos = msg.yPos;
    }
    else {
      resolved.yPos = 0.0
    }

    if (msg.heading !== undefined) {
      resolved.heading = msg.heading;
    }
    else {
      resolved.heading = 0.0
    }

    return resolved;
    }
};

module.exports = MowerStats;
