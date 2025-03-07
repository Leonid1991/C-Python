#include <iostream>;


int function(int a, int b)
{
	return a + b;
}

extern "C"
{
	int Function(int a,int b)
	{
		 return function(a, b);
	}
}