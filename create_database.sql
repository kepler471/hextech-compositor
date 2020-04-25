CREATE TABLE summoners
/*
persons will be the reference table for summoners and account info
there mayb be non-static data, such as current ranks and summoner levels, 
but there should be an accompanying revisionDate to give a timestamp that
is near to when the data was collected.
*/
(
  summonerName    character varying(16),
  summonerId      character varying(100) primary key,
  accountId       character varying(100),
  puuid           character varying(100),
  queueType       character varying(100),
  leagueId        character varying(100),
  wins            integer,
  losses          integer,
  revisionDate    timestamp,
  tier            character varying(10),
  rank            character varying(5),
  summonerLevel   integer
);