// Generated by gencpp from file bond/Status.msg
// DO NOT EDIT!


#ifndef BOND_MESSAGE_STATUS_H
#define BOND_MESSAGE_STATUS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace bond
{
template <class ContainerAllocator>
struct Status_
{
  typedef Status_<ContainerAllocator> Type;

  Status_()
    : header()
    , id()
    , instance_id()
    , active(false)
    , heartbeat_timeout(0.0)
    , heartbeat_period(0.0)  {
    }
  Status_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , id(_alloc)
    , instance_id(_alloc)
    , active(false)
    , heartbeat_timeout(0.0)
    , heartbeat_period(0.0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _id_type;
  _id_type id;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _instance_id_type;
  _instance_id_type instance_id;

   typedef uint8_t _active_type;
  _active_type active;

   typedef float _heartbeat_timeout_type;
  _heartbeat_timeout_type heartbeat_timeout;

   typedef float _heartbeat_period_type;
  _heartbeat_period_type heartbeat_period;




  typedef boost::shared_ptr< ::bond::Status_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::bond::Status_<ContainerAllocator> const> ConstPtr;

}; // struct Status_

typedef ::bond::Status_<std::allocator<void> > Status;

typedef boost::shared_ptr< ::bond::Status > StatusPtr;
typedef boost::shared_ptr< ::bond::Status const> StatusConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::bond::Status_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::bond::Status_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace bond

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'bond': ['/home/pi/catkin_ws/src/bond_core/bond/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::bond::Status_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::bond::Status_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::bond::Status_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::bond::Status_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::bond::Status_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::bond::Status_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::bond::Status_<ContainerAllocator> >
{
  static const char* value()
  {
    return "eacc84bf5d65b6777d4c50f463dfb9c8";
  }

  static const char* value(const ::bond::Status_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xeacc84bf5d65b677ULL;
  static const uint64_t static_value2 = 0x7d4c50f463dfb9c8ULL;
};

template<class ContainerAllocator>
struct DataType< ::bond::Status_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bond/Status";
  }

  static const char* value(const ::bond::Status_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::bond::Status_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n\
string id  # ID of the bond\n\
string instance_id  # Unique ID for an individual in a bond\n\
bool active\n\
\n\
# Including the timeouts for the bond makes it easier to debug mis-matches\n\
# between the two sides.\n\
float32 heartbeat_timeout\n\
float32 heartbeat_period\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
";
  }

  static const char* value(const ::bond::Status_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::bond::Status_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.id);
      stream.next(m.instance_id);
      stream.next(m.active);
      stream.next(m.heartbeat_timeout);
      stream.next(m.heartbeat_period);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Status_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::bond::Status_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::bond::Status_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "id: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.id);
    s << indent << "instance_id: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.instance_id);
    s << indent << "active: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.active);
    s << indent << "heartbeat_timeout: ";
    Printer<float>::stream(s, indent + "  ", v.heartbeat_timeout);
    s << indent << "heartbeat_period: ";
    Printer<float>::stream(s, indent + "  ", v.heartbeat_period);
  }
};

} // namespace message_operations
} // namespace ros

#endif // BOND_MESSAGE_STATUS_H
