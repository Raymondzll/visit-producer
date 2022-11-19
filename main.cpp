#include <bits/stdc++.h>
using namespace std;
string a,b,c,d;
int main(int argc,char *argv[]){
	a="5";
	if(argc>=2)a=argv[1];
	if(argc>=3)b=argv[2];
	if(argc>=4)c=argv[3];
	if(argc>=5)d=argv[4];
	stringstream ss(a);
	int t;ss>>t;
	for(int i=1;i<=t;i++){cout<<"started ";
		system(("start pythonw ask.py "+b+" "+c+" "+d).c_str());
	}
	return 0;
}

