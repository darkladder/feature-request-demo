-- Adminer 4.6.3 PostgreSQL dump

DROP TABLE IF EXISTS "feature_requests";
DROP SEQUENCE IF EXISTS feature_requests_id_seq;
CREATE SEQUENCE feature_requests_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."feature_requests" (
    "id" integer DEFAULT nextval('feature_requests_id_seq') NOT NULL,
    "title" text NOT NULL,
    "description" text NOT NULL,
    "client" text NOT NULL,
    "client_priority" smallint NOT NULL,
    "target_date" date NOT NULL,
    "product_area" text NOT NULL
) WITH (oids = false);

TRUNCATE "feature_requests";
INSERT INTO "feature_requests" ("id", "title", "description", "client", "client_priority", "target_date", "product_area") VALUES
(39,	'Feature request 2',	'Test description',	'Client B',	1,	'2018-08-01',	'Billing'),
(40,	'Another feature request',	'Test description........',	'Client C',	1,	'2018-08-01',	'Billing'),
(41,	'hello_new_title',	'abcdeabc',	'Client A',	2,	'2018-04-28',	'Agents'),
(38,	'Feature request 1',	'A description of this feature request',	'Client A',	1,	'2018-08-01',	'Claims');

-- 2018-08-01 20:34:20.015283+00