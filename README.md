# Real estate consultant project under the command line in Python

## definitions
__Each estate can have three different types__
- House
- Apartment
- Store

__Each estate has the following__
- User: first name & last name & phone number
- area
- rooms count
- built year
- region
- address

### In two different types
__Apartment__
- has elevator
- has parking
- floor
  
__House__
- has yard
- floors count

### Real estate consultant files can be of two different types
__Sell__
- price per meter
- discountable
- convertable

__Rent__
- initial price
- monthly price
- convertable
- discountable

### Requirements
- We must be able to see a report of the data in the system.
- We must be able to see the list of advertisements in the system.
- We should be able to search by specifying the file type based on the following fields: <br />
Region <br /> Price <br /> Rooms count <br /> Area

### Note
- All entities must have a unique counter
- if a property is both for rent and for sale, it must be registered twice
- All classes must have a `object_list` as a storage space
- Assume that the data has already been entered into the system.
