CREATE TABLE native_kernel.kernel_instances (
    instance_id text PRIMARY KEY,
    profile_id text NOT NULL,
    evidence_lineage text NOT NULL,
    last_global_seq bigint NOT NULL DEFAULT 0 CHECK (last_global_seq >= 0),
    writer_epoch bigint NOT NULL DEFAULT 0 CHECK (writer_epoch >= 0),
    last_event_hash text,
    created_at timestamptz NOT NULL DEFAULT transaction_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT transaction_timestamp(),
    CHECK (last_event_hash IS NULL OR last_event_hash ~ '^nke1:[0-9a-f]{64}$')
);

CREATE TABLE native_kernel.writer_leases (
    instance_id text PRIMARY KEY REFERENCES native_kernel.kernel_instances(instance_id) ON DELETE RESTRICT,
    owner_id text NOT NULL,
    epoch bigint NOT NULL CHECK (epoch > 0),
    expires_at timestamptz NOT NULL,
    updated_at timestamptz NOT NULL DEFAULT transaction_timestamp()
);

CREATE TABLE native_kernel.stream_counters (
    instance_id text NOT NULL REFERENCES native_kernel.kernel_instances(instance_id) ON DELETE RESTRICT,
    stream_id text NOT NULL,
    last_stream_seq bigint NOT NULL DEFAULT 0 CHECK (last_stream_seq >= 0),
    PRIMARY KEY (instance_id, stream_id)
);

CREATE TABLE native_kernel.events (
    instance_id text NOT NULL REFERENCES native_kernel.kernel_instances(instance_id) ON DELETE RESTRICT,
    global_seq bigint NOT NULL CHECK (global_seq > 0),
    event_id text NOT NULL,
    command_id text NOT NULL,
    command_contract text NOT NULL,
    idempotency_key text NOT NULL,
    command_digest text NOT NULL,
    stream_id text NOT NULL,
    stream_seq bigint NOT NULL CHECK (stream_seq > 0),
    actor_ref text NOT NULL,
    authority_ref text NOT NULL,
    recorded_at timestamptz(0) NOT NULL,
    event_type text NOT NULL CHECK (event_type IN ('ADMIT','LINK','UTILIZED','SUPERSEDED','ERASED')),
    schema_version text NOT NULL,
    payload jsonb NOT NULL,
    payload_canonical bytea NOT NULL,
    prev_global_hash text NOT NULL,
    payload_hash text NOT NULL CHECK (payload_hash ~ '^nkp1:[0-9a-f]{64}$'),
    event_hash text NOT NULL CHECK (event_hash ~ '^nke1:[0-9a-f]{64}$'),
    envelope_canonical bytea NOT NULL,
    writer_epoch bigint NOT NULL CHECK (writer_epoch > 0),
    PRIMARY KEY (instance_id, global_seq),
    UNIQUE (instance_id, event_id),
    UNIQUE (instance_id, stream_id, stream_seq),
    UNIQUE (instance_id, event_hash),
    CHECK (prev_global_hash = 'GENESIS' OR prev_global_hash ~ '^nke1:[0-9a-f]{64}$')
);

CREATE TABLE native_kernel.idempotency_records (
    instance_id text NOT NULL,
    command_contract text NOT NULL,
    idempotency_key text NOT NULL,
    command_digest text NOT NULL,
    global_seq bigint NOT NULL,
    event_hash text NOT NULL,
    created_at timestamptz NOT NULL DEFAULT transaction_timestamp(),
    PRIMARY KEY (instance_id, command_contract, idempotency_key),
    FOREIGN KEY (instance_id, global_seq)
        REFERENCES native_kernel.events(instance_id, global_seq)
        ON DELETE RESTRICT,
    CHECK (event_hash ~ '^nke1:[0-9a-f]{64}$')
);

CREATE INDEX nk_events_stream_order_idx
    ON native_kernel.events(instance_id, stream_id, stream_seq);
CREATE INDEX nk_events_recorded_at_idx
    ON native_kernel.events(instance_id, recorded_at);
