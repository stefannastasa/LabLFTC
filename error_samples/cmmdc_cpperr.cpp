#include<iostream>
struct pereche{
	int n;
	int m;
}p;
int main(){
	std::cin>>n;
	std::cin>>m;
	//eroare punct si virgula
	int nr_mic
	if( p.n > p.m ){
		nr_mic = p.m;
	}
	if(p.m >= p.n){
		nr_mic = p.n;
	}
	//eroare virgula
	int i cmmdc;
	cmmdc=1;
	for( i = nr_mic; i >= 2; i=i-1){
		if( n % i == 0 && m % i == 0){
			cmmdc=i;	
		}
	}
	std::cout<<cmmdc<<'\n';
}
