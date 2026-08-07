CREATE TABLE native_kernel.operation_receipts (
    receipt_id text PRIMARY KEY,
    operation_type text NOT NULL CHECK (operation_type IN ('REPLAY','PROJECTION_REBUILD')),
    instance_id text NOT NULL REFERENCES native_kernel.kernel_instances(instance_id) ON DELETE RESTRICT,
    projection_name text,
    projection_generation bigint CHECK (projection_generation IS NULL OR projection_generation > 0),
    event_count bigint NOT NULL CHECK (event_count >= 0),
    first_global_seq bigint NOT NULL CHECK (first_global_seq >= 0),
    last_global_seq bigint NOT NULL CHECK (last_global_seq >= 0),
    last_event_hash text,
    reducer_version text NOT NULL,
    target_schema_version text NOT NULL,
    state_digest text NOT NULL CHECK (state_digest ~ '^nks0:[0-9a-f]{64}$'),
    known_limits jsonb NOT NULL CHECK (jsonb_typeof(known_limits) = 'array'),
    created_at timestamptz(0) NOT NULL,
    claims_truth_established boolean NOT NULL DEFAULT false CHECK (NOT claims_truth_established),
    claims_external_authenticity boolean NOT NULL DEFAULT false CHECK (NOT claims_external_authenticity),
    claims_complete_integrity boolean NOT NULL DEFAULT false CHECK (NOT claims_complete_integrity),
    claims_complete_erasure boolean NOT NULL DEFAULT false CHECK (NOT claims_complete_erasure),
    receipt_hash text NOT NULL UNIQUE CHECK (receipt_hash ~ '^nkr0:[0-9a-f]{64}$'),
    receipt_canonical bytea NOT NULL,
    CHECK (last_event_hash IS NULL OR last_event_hash ~ '^nke1:[0-9a-f]{64}$'),
    CHECK (
        (operation_type = 'REPLAY' AND projection_name IS NULL AND projection_generation IS NULL)
        OR
        (operation_type = 'PROJECTION_REBUILD' AND projection_name IS NOT NULL AND projection_generation IS NOT NULL)
    ),
    CHECK (
        (event_count = 0 AND first_global_seq = 0 AND last_global_seq = 0 AND last_event_hash IS NULL)
        OR
        (event_count > 0 AND first_global_seq = 1 AND last_global_seq = event_count AND last_event_hash IS NOT NULL)
    )
);

CREATE INDEX nk_operation_receipts_instance_created_idx
    ON native_kernel.operation_receipts(instance_id, created_at, receipt_id);

CREATE TABLE native_kernel.projections (
    instance_id text NOT NULL REFERENCES native_kernel.kernel_instances(instance_id) ON DELETE RESTRICT,
    projection_name text NOT NULL,
    reducer_version text NOT NULL,
    target_schema_version text NOT NULL,
    generation bigint NOT NULL CHECK (generation > 0),
    last_global_seq bigint NOT NULL CHECK (last_global_seq >= 0),
    last_event_hash text,
    state jsonb NOT NULL,
    state_canonical bytea NOT NULL,
    state_digest text NOT NULL CHECK (state_digest ~ '^nks0:[0-9a-f]{64}$'),
    receipt_id text NOT NULL REFERENCES native_kernel.operation_receipts(receipt_id) ON DELETE RESTRICT,
    rebuilt_at timestamptz(0) NOT NULL,
    PRIMARY KEY (instance_id, projection_name),
    CHECK (last_event_hash IS NULL OR last_event_hash ~ '^nke1:[0-9a-f]{64}$'),
    CHECK (
        (last_global_seq = 0 AND last_event_hash IS NULL)
        OR
        (last_global_seq > 0 AND last_event_hash IS NOT NULL)
    )
);
