#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	char text;
	while (scanf("%c", &text) != -1) {
		printf("%c", text);
	}

	return 0;
}