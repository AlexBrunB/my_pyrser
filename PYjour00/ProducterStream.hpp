//
// ProducterStream.hpp for ProducterStream in /home/abrun/delivery/Tek2/Python/PYjour00
// 
// Made by Alexandre Brun
// Login   <abrun@epitech.net>
// 
// Started on  Mon Jun  5 09:38:18 2017 Alexandre Brun
// Last update Mon Jun  5 12:49:46 2017 Alexandre Brun
//

#ifndef _PRODUCTERSTREAM_HPP_
# define _PRODUCTERSTREAM_HPP_

# define MY_BUFF	0x1000
# include <string>
# include <iostream>
# include <fstream>
# include <cstring>

class ProducterStream
{
public:
  
  ProducterStream();
  ~ProducterStream();
  
  std::string nextString();
  bool	loadFile(char *path);
  bool	loadStdin();
  char	buffer[MY_BUFF + 1];
  
private:
  std::ifstream my_ifstream;
};

#endif /* _PRODUCTERSTREAM_HPP_ */
