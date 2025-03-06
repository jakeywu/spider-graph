CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    mobile VARCHAR(20) UNIQUE,
    email VARCHAR(255) UNIQUE,
    password_hash VARCHAR(128),
    nickname VARCHAR(50) NOT NULL,
    full_name VARCHAR(100),
    description TEXT,
    is_active BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    CHECK (mobile IS NOT NULL OR email IS NOT NULL)
);

CREATE TABLE login_histories (
    id SERIAL PRIMARY KEY,
    user_id UUID NOT NULL REFERENCES users(id),
    login_at TIMESTAMP DEFAULT NOW(),
    ip_address INET NOT NULL,
    login_method VARCHAR(20) NOT NULL
);