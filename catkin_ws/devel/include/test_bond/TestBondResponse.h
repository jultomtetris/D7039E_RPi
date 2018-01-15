// Generated by gencpp from file test_bond/TestBondResponse.msg
// DO NOT EDIT!


#ifndef TEST_BOND_MESSAGE_TESTBONDRESPONSE_H
#define TEST_BOND_MESSAGE_TESTBONDRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace test_bond
{
template <class ContainerAllocator>
struct TestBondResponse_
{
  typedef TestBondResponse_<ContainerAllocator> Type;

  TestBondResponse_()
    {
    }
  TestBondResponse_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }






  typedef boost::shared_ptr< ::test_bond::TestBondResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::test_bond::TestBondResponse_<ContainerAllocator> const> ConstPtr;

}; // struct TestBondResponse_

typedef ::test_bond::TestBondResponse_<std::allocator<void> > TestBondResponse;

typedef boost::shared_ptr< ::test_bond::TestBondResponse > TestBondResponsePtr;
typedef boost::shared_ptr< ::test_bond::TestBondResponse const> TestBondResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::test_bond::TestBondResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::test_bond::TestBondResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace test_bond

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::test_bond::TestBondResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::test_bond::TestBondResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::test_bond::TestBondResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::test_bond::TestBondResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::test_bond::TestBondResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::test_bond::TestBondResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::test_bond::TestBondResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::test_bond::TestBondResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::test_bond::TestBondResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "test_bond/TestBondResponse";
  }

  static const char* value(const ::test_bond::TestBondResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::test_bond::TestBondResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n\
";
  }

  static const char* value(const ::test_bond::TestBondResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::test_bond::TestBondResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct TestBondResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::test_bond::TestBondResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::test_bond::TestBondResponse_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // TEST_BOND_MESSAGE_TESTBONDRESPONSE_H
