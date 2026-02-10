function solution(numbers) {
    const N = numbers.length;
    const visited = Array(N).fill(false);
    const primes = new Set();

    function isPrime(n) {
        if (n < 2) return false;
        for (let i = 2; i * i <= n; i++) {
            if (n % i === 0) return false;
        }
        return true;
    }

    function dfs(current) {
        if (current.length > 0) {
            const num = Number(current);
            if (isPrime(num)) {
                primes.add(num);
            }
        }

        if (current.length === N) return;

        for (let i = 0; i < N; i++) {
            if (visited[i]) continue;

            visited[i] = true;
            dfs(current + numbers[i]);
            visited[i] = false;
        }
    }

    dfs('');
    return primes.size;
}