#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main(){

   string s= "aabbabaabb";
   vector<int>v;
   int l=0, counter=1;
   int sz= v.size();
   int w1, w2, w3, mx=1e-9, i,j;
   bool flag = (s[0]=='a')? 1 : 0;
   bool flag2 = (s[sz-1]=='a')? 1 : 0;

   while(l<s.size()){
    if(s[l]==s[++l])
        counter++;
    else{
        v.push_back(counter);
        counter=1;
    }
   }
    if(v.size()<3)
        return s.size();
    
    else if(v.size()==3)
        if (flag)
            return  s.size();
        else
            return max( s.size()-v[0],  s.size()-v[2]);
    vector<int>prefx;
    for (int i=0; i<v.size(); i++){
        prefx.push_back(v[i]);
        if(i>1)
            prefx[i]+=prefx[i-2];
    }

    if(!flag &&!flag2){
        mx= max(prefx[0]+prefx[sz-2],v[sz-1]+prefx[sz-2]);
         i=1, j=sz-2;
    }
    else if(flag && !flag2){
        mx=max(mx, v[sz-1]+prefx[sz-2]);
         i=0, j=sz-2;
    }
    else if(!flag && flag2){
        mx=max(mx, prefx[0]+prefx[sz-2]);
         i=1, j=sz-1;
    }
    else
        i=0, j=sz-1;
    
    for(; i <prefx.size();i+=2){
        while(j>=i){
            w1= prefx[i];
            w2= prefx[--j]-prefx[i+1]+v[i+1];
            w3= prefx[sz-1]-prefx[--j]+v[j];
            mx= max(mx, w1+w2+w3);
        }
    }
    
    cout<<mx<< endl;
}


