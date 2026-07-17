# Check stability conditions for the state-space model
import numpy as np
from scipy.linalg import eigvals

def check_boundedness(A):
    """
    Check if system is bounded: all eigenvalues inside unit circle (discrete-time)
    Returns True if spectral radius < 1
    """
    eig = eigvals(A)
    rho = np.max(np.abs(eig))
    return rho < 1.0, rho

def check_lipschitz(A, b_bound=1.0):
    """
    Check Lipschitz condition: ||A|| < 1 for some induced norm
    Using spectral norm (largest singular value)
    """
    # For discrete-time linear system, Lipschitz constant of f(x)=Ax+b is ||A||
    # We use spectral norm as approximation
    U, s, Vh = np.linalg.svd(A)
    spectral_norm = np.max(s)
    return spectral_norm < 1.0, spectral_norm

def check_forward_invariance(A, B, constraint_set):
    """
    Check if set {x | Cx <= d} is forward invariant
    For simplicity, we check if the origin is stable and trajectories remain bounded
    This is a simplified check - actual invariance requires more complex analysis
    """
    # Placeholder: for now, just check boundedness
    stable, rho = check_boundedness(A)
    return stable, rho

def check_contraction(A, epsilon=0.1):
    """
    Check if map is contraction: ||A|| < 1 - epsilon
    """
    U, s, Vh = np.linalg.svd(A)
    spectral_norm = np.max(s)
    return spectral_norm < (1.0 - epsilon), spectral_norm

def check_iss(A, B, gamma=0.5):
    """
    Check input-to-state stability: there exists beta in KL and gamma in K such that
    ||x(k)|| <= beta(||x(0)||,k) + gamma(sup_{0<=i<k} ||u(i)||)
    For linear discrete-time: sufficient condition is spectral radius of A < 1
    and we can compute the gain from u to x
    """
    # Check internal stability
    stable_A, rho_A = check_boundedness(A)
    if not stable_A:
        return False, rho_A, None
    
    # Compute L2 gain from u to x (simplified)
    # For discrete-time Lyapunov: solve A'PA - P + C'C = 0 for observability
    # Here we compute H2 norm approximation
    try:
        # Solve discrete Lyapunov for controllability gramian
        # P = A P A' + B B'
        n = A.shape[0]
        P = np.zeros((n, n))
        max_iter = 1000
        tol = 1e-6
        for i in range(max_iter):
            P_next = A @ P @ A.T + B @ B.T
            if np.max(np.abs(P_next - P)) < tol:
                P = P_next
                break
            P = P_next
        
        # H2 norm squared = trace(C P C') but we don't have C here
        # Instead, we compute the gain from u to state x
        # Gain ≈ sqrt(trace(P)) when B is input matrix
        gain = np.sqrt(np.trace(P))
        return True, rho_A, gain
    except:
        return False, rho_A, None

def analyze_stability_matrices(A_list, B_list):
    """
    Analyze stability for a list of subsystem matrices
    """
    results = []
    for i, (A, B) in enumerate(zip(A_list, B_list)):
        print(f"\nSubsystem {i+1}:")
        print(f"A = \n{A}")
        print(f"B = \n{B}")
        
        # Boundedness
        stable, rho = check_boundedness(A)
        print(f"  Bounded (rho<1): {stable}, spectral radius = {rho:.4f}")
        
        # Lipschitz
        lip, lip_norm = check_lipschitz(A)
        print(f"  Lipschitz (||A||<1): {lip}, spectral norm = {lip_norm:.4f}")
        
        # Contraction
        con, con_norm = check_contraction(A, epsilon=0.05)
        print(f"  Contraction (||A||<0.95): {con}, spectral norm = {con_norm:.4f}")
        
        # ISS
        iss, rho_A, gain = check_iss(A, B)
        if gain is not None:
            print(f"  ISS (stable A): {iss}, rho={rho_A:.4f}, gain≈{gain:.4f}")
        else:
            print(f"  ISS (stable A): {iss}, rho={rho_A:.4f}")
        

        # Overall assessment
        if stable and lip:
            print("  >>> SUBSYSTEM IS STABLE AND WELL-BEHAVED <<<")
        else:
            print("  >>> SUBSYSTEM MAY HAVE STABILITY ISSUES <<<")
        
        results.append({
            'subsystem': i+1,
            'stable': stable,
            'spectral_radius': rho,
            'lipschitz': lip,
            'spectral_norm': lip_norm,
            'iss': iss
        })
    
    return results

if __name__ == "__main__":
    # Example from simulate_pipeline.py
    A1 = np.array([[0.9]])
    B1 = np.array([[0.1]])
    
    A2 = np.array([[0.8]])
    B2 = np.array([[0.2]])
    
    A_list = [A1, A2]
    B_list = [B1, B2]
    
    print("Stability Analysis of Subsystems")
    print("=" * 50)
    results = analyze_stability_matrices(A_list, B_list)
    
    # Summary
    print("\n\nSUMMARY")
    print("=" * 50)
    all_stable = all(r['stable'] for r in results)
    print(f"All subsystems internally stable: {all_stable}")
    
    # For coupled system, we would need to analyze the overall system matrix
    # This is more complex and depends on the coupling structure
    print("\nNote: For coupled systems, stability analysis must consider the interconnection structure.")
    print("The paper provides sufficient conditions for the overall closed-loop system.")