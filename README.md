# Priority-based Emergency Distribution Algorithm

## Overview
This algorithm is an adaptation of network flow techniques for emergency supply distribution, specifically designed to handle priority-based routing in disaster response scenarios. It optimizes the distribution of emergency supplies by considering both time constraints and the varying urgency levels of different affected areas.

## Key Features
- Priority-based routing for emergency supplies
- Multiple path optimization
- Consideration of travel and processing times
- Capacity constraints for transportation routes
- Flexible priority assignment for affected areas

## Prerequisites
- Python 3.6 or higher
- Basic Python packages: `heapq`, `collections`

## Installation
1. Clone this repository
2. No additional package installation is required beyond Python's standard library

## Usage

### Basic Setup
```python
from emergency_network import EmergencyNetwork

# Define your network structure
vertices = {'source', 'location1', 'location2', 'destination'}
edges = {('source', 'location1'), ('location1', 'destination')}

# Define priorities (higher number = higher priority)
priorities = {
    'location1': 1,  # Low priority
    'location2': 3   # High priority
}

# Create network instance
network = EmergencyNetwork(vertices, edges, priorities)
```

### Adding Network Details
```python
# Add routes with capacities and travel times
network.add_edge('source', 'location1', capacity=10, travel_time=2)
network.add_edge('location1', 'destination', capacity=5, travel_time=1)

# Set processing times at locations
network.set_vertex_residence_time('location1', time=1)
```

### Running the Distribution
```python
# Distribute 20 units of supplies
paths, times, total_flow = network.distribute_supplies('source', 'destination', 20)
```

## Understanding the Output
- `paths`: List of paths taken and their flow amounts
- `times`: Time taken for each path
- `total_flow`: Total amount of supplies successfully distributed

## Safety and Ethical Considerations

### Important Notes
1. This algorithm is designed as an undergraduate project only and should not be the sole decision-maker in emergency situations
2. Local expertise and human judgment should always take precedence

### Best Practices
- Regularly update priority levels based on current needs
- Verify route capacities and travel times frequently
- Consider alternative routes for redundancy
- Maintain backup plans for system failures

## Limitations
1. Assumes static network conditions
2. Does not account for:
   - Dynamic changes in road conditions
   - Weather impacts
   - Real-time traffic

## Example Scenario
```python
def example_usage():
    # Network setup
    vertices = {'s', 'v1', 'v2', 'v3', 'v4', 't'}
    edges = {('s','v1'), ('s','v2'), ('v1','v3'), ('v2','v3'), ('v3','t')}
    priorities = {'v1': 1, 'v2': 2, 'v3': 3, 'v4': 1, 't': 3}
    
    network = EmergencyNetwork(vertices, edges, priorities)
    
    # Add routes
    network.add_edge('s', 'v1', capacity=10, travel_time=2)
    network.add_edge('s', 'v2', capacity=8, travel_time=3)
    
    # Add processing times
    network.set_vertex_residence_time('v1', 1)
    network.set_vertex_residence_time('v2', 1)
    
    # Run distribution
    paths, times, total_flow = network.distribute_supplies('s', 't', 15)
```

## Contributing
Contributions to improve the algorithm are welcome. Please ensure that any modifications:
- Maintain or improve safety considerations
- Include appropriate documentation
- Add relevant test cases
- Consider real-world application constraints

## Priority Model Design

### Priority System Overview
The priority system was designed to balance two critical factors in emergency response:
1. Time efficiency of supply delivery
2. Urgency level of affected areas

### Priority Scale
- Priorities are assigned on a numerical scale (1 to N)
- Higher numbers indicate higher priority (e.g., 3 is more urgent than 1)
- The scale is flexible and can be adjusted based on specific needs
- Default priority is 1 for unassigned locations

### Priority Factor Calculation
The algorithm uses a priority factor that:
- Transforms priority levels into routing weights
- Adjusts effective travel times based on location urgency
- Is calculated using the formula: 
  ```python
  priority_factor = (max_priority - vertex_priority + 1) / max_priority
  ```

### Impact on Route Selection
- Higher priority locations get lower priority factors
- Lower priority factors reduce effective travel times
- This makes high-priority routes more attractive to the pathfinding algorithm
- Example:
  ```
  For max_priority = 4:
  Priority 4 (Highest) → Factor = 0.25
  Priority 3          → Factor = 0.50
  Priority 2          → Factor = 0.75
  Priority 1 (Lowest) → Factor = 1.00
  ```

### Dynamic Priority Considerations
The current implementation supports:
- Static priority assignments
- Manual priority updates
- Different priority scales for different scenarios

Future enhancements could include:
- Dynamic priority adjustment based on supply levels
- Time-based priority evolution
- Multi-factor priority calculation


### Limitations and Considerations
- Priorities are relative within the system
- The model assumes priorities remain constant during distribution
- May need adjustment for specific emergency types


## Acknowledgments
This implementation is adapted from the research paper "The Distribution of Emergency Supplies Based on Network Flow" with additional priority considerations for disaster response scenarios.

## Contact
For questions and support, please open an issue in the repository.

## References
1. Original Network Flow Algorithm: Zheng Jie, QinYong-bin, Wei Jia-yin
