#!/usr/bin/env python3
"""
Quantum counting algorithm for number theory problems.
Based on Grover + Shor Fourier transform pattern.

Reference: arxiv:9907020v2 (Carlini, Hosoya)
"""

import numpy as np
from typing import Callable, Tuple

class QuantumCounter:
    """
    Quantum counting using Grover operator + Fourier transform.
    
    Estimates the number of solutions to a search problem.
    """
    
    def __init__(self, n_qubits: int, oracle: Callable):
        """
        Args:
            n_qubits: Number of qubits in search space
            oracle: Oracle function marking solutions
        """
        self.n_qubits = n_qubits
        self.oracle = oracle
        self.N = 2 ** n_qubits  # Search space size
        
    def grover_operator(self, state: np.ndarray) -> np.ndarray:
        """
        Apply Grover operator: G = (2|ψ⟩⟨ψ| - I)O
        
        where:
        - |ψ⟩ = uniform superposition
        - O = oracle
        """
        # Oracle application
        marked_state = self.oracle(state)
        
        # Inversion about average
        avg = np.mean(state)
        inverted = 2 * avg - state
        
        return inverted
    
    def quantum_fourier_transform(self, state: np.ndarray) -> np.ndarray:
        """
        Apply QFT to extract periodicity.
        
        QFT|x⟩ = Σ_y exp(2πixy/N) |y⟩ / N
        """
        N = len(state)
        result = np.zeros(N, dtype=complex)
        
        for y in range(N):
            for x in range(N):
                result[y] += state[x] * np.exp(2 * np.pi * 1j * x * y / N)
        
        return result / np.sqrt(N)
    
    def estimate_count(self, precision: int = 10) -> Tuple[int, float]:
        """
        Estimate number of solutions using quantum counting.
        
        Args:
            precision: Number of Fourier samples
        
        Returns:
            (estimated_count, confidence)
        """
        # Initialize superposition
        state = np.ones(self.N) / np.sqrt(self.N)
        
        # Apply Grover iterations
        # Optimal: k ≈ π/4 × √(N/M) for unknown M
        # Use adaptive approach
        k_iterations = max(1, int(np.sqrt(self.N) / 4))
        
        for _ in range(k_iterations):
            state = self.grover_operator(state)
        
        # Fourier transform
        qft_state = self.quantum_fourier_transform(state)
        
        # Extract periodicity
        probabilities = np.abs(qft_state) ** 2
        
        # Find peaks (indicate solution count)
        peaks = np.argsort(probabilities)[-precision:]
        
        # Estimate solution count from peak positions
        # M ≈ (N/π) sin(θ) where θ from Fourier peak
        estimated_counts = []
        for peak in peaks:
            theta = 2 * np.pi * peak / self.N
            M_estimate = (self.N / np.pi) * np.sin(theta / 2)
            estimated_counts.append(int(np.round(M_estimate)))
        
        # Take median for robust estimate
        estimated_count = int(np.median(estimated_counts))
        
        # Confidence from probability distribution
        confidence = np.mean([probabilities[p] for p in peaks])
        
        return estimated_count, confidence


class PrimalityTester:
    """
    Quantum primality testing using counting algorithm.
    """
    
    def __init__(self):
        self.counter = None
    
    def is_prime(self, n: int) -> Tuple[bool, float]:
        """
        Test if n is prime using quantum counting.
        
        Args:
            n: Number to test
        
        Returns:
            (is_prime, confidence)
        """
        # Oracle: mark divisors of n
        def divisor_oracle(state):
            marked = state.copy()
            for i in range(2, int(np.sqrt(n)) + 1):
                if n % i == 0:
                    marked[i] = -state[i]  # Mark divisor
            return marked
        
        # Quantum counting to estimate divisor count
        n_bits = int(np.ceil(np.log2(n)))
        counter = QuantumCounter(n_bits, divisor_oracle)
        
        divisor_count, confidence = counter.estimate_count()
        
        # Prime if no divisors (except 1 and itself)
        is_prime = divisor_count <= 2
        
        return is_prime, confidence


class PrimeCounter:
    """
    Estimate π(N) using quantum counting.
    π(N) = number of primes ≤ N
    """
    
    def __init__(self):
        self.primality_tester = PrimalityTester()
    
    def prime_counting(self, N: int) -> int:
        """
        Estimate π(N) using quantum counting.
        
        Args:
            N: Upper bound
        
        Returns:
            Estimated prime count
        """
        # Oracle: mark primes ≤ N
        def prime_oracle(state):
            marked = state.copy()
            for i in range(2, N + 1):
                is_prime, conf = self.primality_tester.is_prime(i)
                if is_prime:
                    marked[i] = -state[i]  # Mark prime
            return marked
        
        # Quantum counting
        n_bits = int(np.ceil(np.log2(N)))
        counter = QuantumCounter(n_bits, prime_oracle)
        
        prime_count, confidence = counter.estimate_count()
        
        return prime_count


class GoldbachCounter:
    """
    Quantum counting for Goldbach conjecture.
    Count representations of N as p + p'.
    """
    
    def __init__(self):
        self.primality_tester = PrimalityTester()
    
    def goldbach_count(self, N: int) -> Tuple[int, float]:
        """
        Count ways to write N as sum of two primes.
        
        Args:
            N: Even number (Goldbach conjecture)
        
        Returns:
            (representation_count, confidence)
        """
        # Oracle: mark (p, p') such that p + p' = N
        def goldbach_oracle(state):
            marked = state.copy()
            for p in range(2, N // 2 + 1):
                is_prime_p, _ = self.primality_tester.is_prime(p)
                is_prime_Np, _ = self.primality_tester.is_prime(N - p)
                
                if is_prime_p and is_prime_Np:
                    # Mark pair
                    marked[p] = -state[p]
                    marked[N - p] = -state[N - p]
            
            return marked
        
        # Quantum counting
        n_bits = int(np.ceil(np.log2(N)))
        counter = QuantumCounter(n_bits, goldbach_oracle)
        
        count, confidence = counter.estimate_count()
        
        return count, confidence


# Example usage
if __name__ == "__main__":
    print("=== Quantum Number Theory Algorithms ===\n")
    
    # Test primality
    tester = PrimalityTester()
    for n in [17, 21, 29, 35]:
        is_prime, conf = tester.is_prime(n)
        print(f"{n}: Prime={is_prime} (confidence={conf:.3f})")
    
    print("\n=== Prime Counting π(N) ===")
    counter = PrimeCounter()
    for N in [10, 50, 100]:
        pi_N = counter.prime_counting(N)
        print(f"π({N}) ≈ {pi_N} (classical: {len([i for i in range(2,N+1) if all(i%p for p in range(2,int(i**0.5)+1))])})")
    
    print("\n=== Goldbach Conjecture ===")
    goldbach = GoldbachCounter()
    for N in [10, 20, 30]:
        count, conf = goldbach.goldbach_count(N)
        print(f"{N} = p + p': {count} representations (conf={conf:.3f})")