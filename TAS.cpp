#include <thread>
#include <chrono>
#include <mutex>
#include <atomic>
#include <iostream>


#define core 16
#define MAX 100000000

using namespace std;
using namespace std::chrono;

atomic <int> sum = 0;

atomic_flag TAS_lock = ATOMIC_FLAG_INIT;

void func_TAS() {
	for (int i = 0; i < (MAX / core); ++i) {
		while (atomic_flag_test_and_set(&TAS_lock));
		sum += 1;
		atomic_flag_clear(&TAS_lock);

	}
}
int main()
{
	thread t1{ func_TAS };
	thread t2{ func_TAS };
	thread t3{ func_TAS };
	thread t4{ func_TAS };
	thread t5{ func_TAS };
	thread t6{ func_TAS };
	thread t7{ func_TAS };
	thread t8{ func_TAS };
	thread t9{ func_TAS };
	thread t10{ func_TAS };
	thread t11{ func_TAS };
	thread t12{ func_TAS };
	thread t13{ func_TAS };
	thread t14{ func_TAS };
	thread t15{ func_TAS };
	thread t16{ func_TAS };


	auto start_t = high_resolution_clock::now();
	t1.join();
	t2.join();
	t3.join();
	t4.join();
	t5.join();
	t6.join();
	t7.join();
	t8.join();
	t9.join();
	t10.join();
	t11.join();
	t12.join();
	t13.join();
	t14.join();
	t15.join();
	t16.join();
	auto du = high_resolution_clock::now() - start_t;

	cout << "Coumputing time is" << duration_cast<milliseconds>(du).count() << "ms,     ";
	cout << "Number of Thread = 16 , SUM = " <<sum << endl;

}