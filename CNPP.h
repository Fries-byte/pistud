#include <stdio.h>
int IE, UI, SIF, PL;
int import(IE="";) {
	if(IE == "main") {
		int input(int UI=""; SIF=false;) {
			if(SIF) {
				scanf("%i", &UI);
			} else {
				scanf("%i", UI);
			}
		}
		int print(PL="";) {
			printf("%i", PL);
		}
	}

	return 0;
}
