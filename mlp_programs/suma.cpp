#include <iostream>

int suma;

int main(){
	suma=0;
	int i, n, temp;
	std::cin>>n;
	for(i=0;i<n;i=i+1){
		std::cin>>temp;
		suma=suma+temp;
	}
	std::cout<<suma<<'\n';
}
