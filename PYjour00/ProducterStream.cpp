//
// ProducterStream.cpp for ProducterStream in /home/abrun/delivery/Tek2/Python/PYjour00
// 
// Made by Alexandre Brun
// Login   <abrun@epitech.net>
// 
// Started on  Mon Jun  5 10:08:43 2017 Alexandre Brun
// Last update Mon Jun  5 12:57:42 2017 Alexandre Brun
//

# include "ProducterStream.hpp"

ProducterStream::ProducterStream() {}

ProducterStream::~ProducterStream() {}

bool ProducterStream::loadFile(char *path)
{
  if (my_ifstream.is_open())
    my_ifstream.open(path, std::ifstream::in);
  return (my_ifstream.is_open());
  
}

bool ProducterStream::loadStdin()
{
  if(my_ifstream.is_open())
    my_ifstream.open("/dev/stdin", std::ifstream::in);
  return (my_ifstream.is_open());
}

std::string ProducterStream::nextString()
{
  std::string my_line = "";
  
  if (my_ifstream.is_open())
    {
      memset(buffer, 0, sizeof(buffer));
      my_ifstream.read(buffer, MY_BUFF - 1);
      buffer[MY_BUFF] = 0;
      my_line += buffer;
    }
  if (!my_ifstream.is_open())
    throw std::runtime_error("File error.");
  
  if (my_ifstream.gcount() == 0)

    throw std::runtime_error("End of file.");

  return (my_line);
  
}
