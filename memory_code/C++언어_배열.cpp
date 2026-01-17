#include <iostream>
using namespace std;    

// 1. C++ 언어의 동적 배열 (
int* a = new int[n];

/*
특징
1. 힙 메모리 할당
2. 생성자 호출 가능 (객체 배열)
3. C++ 스타일 메모리 관리
*/

// 해제 방법 (⚠️ 중요)
delete[] a;


// ❌ 잘못된 예:

delete a;   // 배열인데 delete[] 안 쓰면 undefined behavior

// 이상적인 C++ 동적 배열 사용법: std::vector
#include <vector>

vector<int> vec(n);  // 크기 n인 동적 배열 생성
std::vector<int> a(n)