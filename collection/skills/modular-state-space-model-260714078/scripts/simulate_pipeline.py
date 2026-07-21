# Example simulation of the coupled state-space model
import numpy as np

def simulate_pipeline(A_list, B_list, C_list, u_seq, x0_list):
    """
    Simulate the coupled state-space model.
    
    Args:
        A_list: list of state matrices for each subsystem
        B_list: list of input matrices
        C_list: list of output matrices
        u_seq: sequence of inputs to the first subsystem (sensory input)
        x0_list: list of initial state vectors for each subsystem
    
    Returns:
        x_hist: list of state histories for each subsystem
        y_hist: list of output histories for each subsystem
    """
    n_subsystems = len(A_list)
    n_steps = len(u_seq)
    
    # Initialize state history
    x_hist = [np.zeros((n_steps+1, A_i.shape[0])) for A_i in A_list]
    y_hist = [np.zeros((n_steps+1, C_i.shape[0])) for C_i in C_list]
    
    # Set initial conditions
    for i in range(n_subsystems):
        x_hist[i][0] = x0_list[i]
        y_hist[i][0] = C_list[i] @ x0_list[i]
    
    # Simulate
    for k in range(n_steps):
        # Input to first subsystem is sensory input
        u = np.zeros_like(u_seq[k]) if not isinstance(u_seq[k], np.ndarray) else u_seq[k]
        # For simplicity, we assume u is a scalar and broadcast to appropriate dimension
        # In practice, dimensions must match B_list[0]
        u0 = u_seq[k] if np.isscalar(u_seq[k]) else u_seq[k][0]
        u_vec = np.full(B_list[0].shape[1], u0)  # simple replication
        
        # Propagate through each subsystem
        x_prev = None
        for i in range(n_subsystems):
            if i == 0:
                u_i = u_vec
            else:
                # Input is output of previous subsystem
                u_i = y_hist[i-1][k]  # using previous time step output? Actually should be same time step?
                # For simplicity, we use instantaneous coupling: output of previous at same time step
                # But we need previous state's output. We'll use y from previous step.
                # To avoid algebraic loop, we use previous time step output.
                u_i = y_hist[i-1][k] if k > 0 else np.zeros(C_list[i-1].shape[0])
                # Ensure dimension matches B_list[i]
                if len(u_i) != B_list[i].shape[1]:
                    # Truncate or pad
                    if len(u_i) > B_list[i].shape[1]:
                        u_i = u_i[:B_list[i].shape[1]]
                    else:
                        pad = np.zeros(B_list[i].shape[1] - len(u_i))
                        u_i = np.concatenate([u_i, pad])
            # State update
            x_hist[i][k+1] = A_list[i] @ x_hist[i][k] + B_list[i] @ u_i
            # Output
            y_hist[i][k+1] = C_list[i] @ x_hist[i][k+1]
    
    return x_hist, y_hist

if __name__ == "__main__":
    # Example: 2 subsystems, each scalar state
    A1 = np.array([[0.9]])
    B1 = np.array([[0.1]])
    C1 = np.array([[1.0]])
    
    A2 = np.array([[0.8]])
    B2 = np.array([[0.2]])
    C2 = np.array([[1.0]])
    
    A_list = [A1, A2]
    B_list = [B1, B2]
    C_list = [C1, C2]
    
    # Input: step signal
    u_seq = np.ones(50) * 0.5
    u_seq[:10] = 0.0  # first 10 steps zero
    
    x0_list = [np.array([0.0]), np.array([0.0])]
    
    x_hist, y_hist = simulate_pipeline(A_list, B_list, C_list, u_seq, x0_list)
    
    print("Simulation complete.")
    print("Final state of subsystem 1:", x_hist[0][-1])
    print("Final state of subsystem 2:", x_hist[1][-1])