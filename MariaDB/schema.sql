CREATE DATABASE three_strikes_discord_bot;

USE three_strikes_discord_bot;

CREATE TABLE strikes (
    user_id BIGINT UNSIGNED NOT NULL,
    strike_count INT UNSIGNED NOT NULL DEFAULT 1,
    PRIMARY KEY (user_id)
);
