---
name: information-theoretic-pir
description: "Information-theoretic authenticated private information retrieval (PIR) methodology. Achieves privacy-preserving database queries without computational hardness assumptions, with integrity verification and defense against selective-failure attacks. Use when building privacy-preserving search, secure database access, or authenticated retrieval systems."
---

# Information-Theoretic Authenticated PIR

Private Information Retrieval (PIR) allows clients to retrieve database entries without leaking which entry they're accessing. Information-theoretic PIR achieves this without relying on computational hardness assumptions.

## Core Insight

Standard PIR protects query privacy but not correctness — malicious servers can return wrong answers. Authenticated PIR (APIR) adds integrity but relies on computational assumptions. Information-theoretic PIR with Result Verification (itPIR-RV) achieves integrity without computational assumptions but only provides relaxed query privacy. The new APIR scheme achieves both full query privacy and defense against selective-failure attacks.

## APIR Framework

### Security Properties

1. **Query Privacy**: Server learns nothing about which index is being queried
2. **Integrity**: Client detects any incorrect response from server
3. **Selective-Failure Defense**: Server cannot selectively abort based on query content
4. **Information-Theoretic**: Security holds against computationally unbounded adversaries

### Construction Pattern

```python
class AuthenticatedPIR:
    def __init__(self, num_servers, database):
        self.num_servers = num_servers  # Minimum 2 for itPIR
        self.database = database
        self.auth_keys = self.setup_authentication()
    
    def setup_authentication(self):
        """Setup MAC keys for each database entry."""
        return [generate_mac_key() for _ in range(len(database))]
    
    def query(self, index):
        """Generate PIR queries for multiple servers."""
        queries = []
        for server_id in range(self.num_servers):
            q = generate_pir_query(index, server_id, self.num_servers)
            queries.append(q)
        return queries
    
    def aggregate_response(self, responses, index):
        """Aggregate and verify responses."""
        result = aggregate_pir_responses(responses)
        
        # Verify integrity using authentication tags
        tag = responses[0].auth_tag
        if not verify_mac(result, tag, self.auth_keys[index]):
            raise IntegrityError("Server returned incorrect data")
        
        return result
```

### itPIR Protocol (n servers, t-collusion resistant)

```
Client:
1. Generate random queries q₁,...,qₙ such that Σqᵢ = eᵢ (unit vector at index i)
2. Send qⱼ to server j

Each Server j:
1. Compute response rⱼ = Σₖ qⱼ[k] · DB[k]
2. Send rⱼ back with authentication tag

Client:
1. Compute result = Σⱼ rⱼ
2. Verify authentication tag
3. If valid, result = DB[i]
```

### Selective-Failure Defense

The key innovation: prevent servers from learning whether a query was valid before responding.

```python
class SelectiveFailureDefense:
    """Prevent servers from selectively aborting based on query content."""
    
    def blind_query(self, query, randomness):
        """Blind the query so server can't distinguish valid from random."""
        return blind_pir_query(query, randomness)
    
    def verify_consistency(self, responses):
        """Cross-check responses to detect selective failures."""
        # If server aborts selectively, inconsistency will be detected
        return check_response_consistency(responses)
```

## Application Scenarios

### Secure Medical Record Access
- Retrieve patient records without revealing which patient
- Verify record integrity without computational assumptions

### Financial Data Privacy
- Query market data without revealing trading strategy
- Information-theoretic protection against future quantum attacks

### Legal Discovery
- Search legal databases without revealing case strategy
- Ensure response integrity for legal proceedings

## Security Parameters

| Parameter | Description | Recommended |
|-----------|-------------|-------------|
| n_servers | Number of non-colluding servers | ≥ 2 |
| t | Collusion resistance | t < n/2 |
| mac_bits | Authentication tag size | ≥ 128 |
| field_size | Finite field size | ≥ 2¹²⁸ |

## Pitfalls

- Requires multiple non-colluding servers — single-server itPIR is impossible
- Communication cost grows with database size — use for moderate databases
- Server collusion breaks privacy — ensure physical/organizational separation
- Authentication requires shared key setup — plan key distribution carefully

## References

- arXiv: "Information-Theoretic Authenticated PIR: From PIR-RV To APIR" (ID: 681)
- Chor, Goldreich, Kushilevitz, Sudan (1995) — Original PIR formulation
