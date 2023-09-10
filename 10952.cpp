#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <stdio.h>
using namespace std;

int main() {

	int a, b;
	int num;
	scanf("%d", &num);

	while (num--) {
		scanf("%d,%d", &a, &b);
		printf("%d\n", a + b);
	}

	return 0;
}