# slam_toolbox Parameters (ROS 2) — Notes

This document explains the meaning of parameters used in the following configuration:

```yaml
slam_toolbox:
  ros__parameters:
    # (see yaml file)
```

---

## Core Frame & Topic Settings

| Parameter | Meaning / What it affects |
|---|---|
| `odom_frame` | Odometry reference frame (local, drifts over time). SLAM uses this as the short-term motion reference. |
| `map_frame` | Global map frame produced by SLAM (`map`). Used as the fixed world frame for navigation. |
| `base_frame` | Robot base frame (typically `base_link`). All poses are ultimately expressed relative to this. |
| `scan_topic` | Topic name for incoming `sensor_msgs/LaserScan` data. |
| `use_map_saver` | If `true`, enables map saving functionality (depending on your slam_toolbox workflow). |
| `mode` | `mapping` builds/updates the map while moving (as opposed to localization-only modes). |

---

## Processing Performance

| Parameter | Meaning / What it affects |
|---|---|
| `throttle_scans` | Uses only every N-th scan. `1` means use all scans; higher values reduce CPU but may reduce accuracy. |
| `transform_publish_period` | How often slam_toolbox publishes transforms (seconds). Smaller = more frequent TF updates. |
| `transform_timeout` | Max wait time (seconds) when looking up required TF transforms. Too small can cause TF lookup failures. |
| `tf_buffer_duration` | How long (seconds) TF data is kept in memory for lookups. Longer helps with delayed messages, costs RAM. |
| `scan_queue_size` | Size of the internal scan message queue. Larger helps with bursty scans but increases latency/memory. |
| `stack_size_to_use` | Stack size used by internal threads (bytes). Helpful if you hit stack overflow in heavy workloads. |
| `enable_interactive_mode` | Enables interactive features (e.g., manual interventions such as loop closure tools, if used). |
| `debug_logging` | Enables verbose debug logs. Useful for tuning; can slow things down and produce large logs. |

---

## Map Resolution & Sensor Range

| Parameter | Meaning / What it affects |
|---|---|
| `resolution` | Map grid resolution (meters/cell). `0.05` = 5 cm cells (more detail, more CPU/RAM). |
| `min_laser_range` | Ignore laser points closer than this (meters). Filters out unreliable near-field readings. |
| `max_laser_range` | Ignore laser points farther than this (meters). Limits noise / weak returns at long range. |
| `map_update_interval` | How frequently (seconds) the map is updated/published. Lower = more responsive, higher CPU. |

---

## Solver Configuration (Ceres Solver)

These settings control the **graph optimization** solver used to refine poses and constraints.

| Parameter | Meaning / What it affects |
|---|---|
| `solver_plugin` | Selects the optimization backend. `solver_plugins::CeresSolver` uses Google Ceres. |
| `ceres_linear_solver` | Linear solver type. Sparse Cholesky is typically good for larger sparse problems. |
| `ceres_preconditioner` | Preconditioner for iterative solving / stability. |
| `ceres_trust_strategy` | Trust region strategy. Levenberg–Marquardt is robust and commonly used. |
| `ceres_dogleg_type` | Dogleg method variant (used when dogleg strategy is active). |
| `ceres_loss_function` | Robust loss (e.g., `HUBER`) reduces the influence of outliers in constraints. |

---

## Scan Matching (Local pose estimation)

These settings control how slam_toolbox estimates motion from scan-to-map/scan-to-scan alignment.

| Parameter | Meaning / What it affects |
|---|---|
| `use_scan_matching` | Enables scan matching (core of SLAM front-end). Disabling generally makes SLAM unusable unless external localization is perfect. |
| `use_scan_barycenter` | Whether to use barycenter-based scan feature heuristics (implementation-dependent). Often left `false`. |
| `minimum_time_interval` | Minimum time (seconds) between processed scans for matching. Helps reduce compute load. |
| `minimum_travel_distance` | Minimum translation (meters) before performing scan matching update. |
| `minimum_travel_heading` | Minimum rotation (radians) before performing scan matching update. |

---

## Loop Closure Constraints (Finding when robot returns to old areas)

These parameters influence **nearby link constraints** and **loop closure acceptance thresholds**.

### Neighbor links / scan buffer
| Parameter | Meaning / What it affects |
|---|---|
| `scan_buffer_size` | Number of scans kept for matching/linking. Larger can increase loop/constraint opportunities but uses more memory. |
| `scan_buffer_maximum_scan_distance` | Max distance (meters) considered when buffering/using scans (limits how far back spatially scans are relevant). |
| `link_scan_maximum_distance` | Max distance (meters) to consider linking scans as nearby constraints. |
| `link_match_minimum_response_fine` | Minimum fine match score for accepting a neighbor link constraint. Lower = more constraints but risk of wrong matches. |

### Loop closure enable + thresholds
| Parameter | Meaning / What it affects |
|---|---|
| `do_loop_closing` | Enables loop closure detection/correction. |
| `loop_search_maximum_distance` | Max distance (meters) to search for loop candidates. Larger = more chances, more compute, more false-positive risk. |
| `loop_match_minimum_chain_size` | Minimum number of sequential matches required to accept a loop closure (stability/robustness). |
| `loop_match_maximum_variance_coarse` | Allowed variance during coarse matching. Higher is more tolerant but can admit poorer candidates. |
| `loop_match_minimum_response_coarse` | Coarse match score threshold for loop candidate acceptance. |
| `loop_match_minimum_response_fine` | Fine match score threshold for final acceptance. Higher = stricter loop closures. |

---

## Loop Search Space

| Parameter | Meaning / What it affects |
|---|---|
| `loop_search_space_dimension` | Size (meters) of the search window used for loop correlation. |
| `loop_search_space_resolution` | Translation resolution (meters) for loop search grid. Finer = more compute, potentially more accurate. |
| `loop_search_space_smear_deviation` | Smearing/uncertainty (meters) applied during search to tolerate noise. |

---

## Local Correlation/Matching (Scan-to-map alignment)

These control the correlation-based search used in scan alignment.

| Parameter | Meaning / What it affects |
|---|---|
| `correlation_search_space_dimension` | Local search window size (meters) for scan correlation. |
| `correlation_search_space_resolution` | Step size (meters) used in correlation search. Smaller = more compute, better precision. |
| `correlation_search_space_smear_deviation` | Smearing (meters) to account for uncertainty in scan correlation. |
| `distance_variance_penalty` | Penalizes solutions with high distance variance (tuning weight). |
| `angle_variance_penalty` | Penalizes solutions with high angular variance (tuning weight). |
| `fine_search_angle_offset` | Fine angular step (radians) in local search (≈ 0.2°). |
| `coarse_search_angle_offset` | Coarse angular step (radians) (≈ 20°). |
| `coarse_angle_resolution` | Coarse angular resolution (radians) (≈ 2°). |
| `minimum_angle_penalty` | Lower bound for angle penalty (prevents angle penalty from becoming too small). |
| `minimum_distance_penalty` | Lower bound for distance penalty. |
| `use_response_expansion` | If enabled, expands the search if correlation response is weak (can improve robustness, costs compute). |

---

## Practical tuning hints (quick)

- If CPU is too high: increase `throttle_scans`, increase `minimum_time_interval`, or increase `map_update_interval`.
- If map is noisy / unstable: make loop closure stricter (raise `loop_match_minimum_response_*`), or reduce `loop_search_maximum_distance`.
- If loop closures rarely happen: lower thresholds slightly or increase `loop_search_maximum_distance` / `scan_buffer_size` (watch false positives).

> Note: Exact behavior can vary by slam_toolbox version and sensor characteristics, so treat this as a practical guide rather than a strict spec.