#include <iostream>
#include <ctime>
using std::cout;
using std::endl;
//Declaracion de las funciones
int fibonacci(int N);
float get_time(int N);
//Funcion que devuelve la serie de fibonnaci 
int fibonacci(int N){
	if ( N ==1 || N ==0){//Garantiza los dos primeros numeros de la serie. 
		return N;
	}
	
	else;
		return fibonacci(N-2) + fibonacci (N-1);//Arroja los siguientes valores de la serie
}
int main(){
	int i;//Variable que recorre a fibonacci para 
	int N;//Variable que indica la cantidad de los primeros valores para los cuales quiero que se genere la serie fibonacci
	N = 35;//Se piden los primeros 35 valores
	for(i = 0; i < N; i+=1)//Iteraciones realizadas para que se pase por la función fibonacci 
	{
		float t = get_time(N);//Declaracion de la variable que va a guardar el tiempo para generar los números N de fibonacci
		cout << fibonacci(i) << " " << t << endl;//
	}
}
float get_time(int N){//Función encargada de arrojar los tiempo que se dan en fibonacci
	clock_t t;
	fibonacci(N);
	t = clock();
	t = clock() - t;
	float time = ((float)t); 
	return time;
}

