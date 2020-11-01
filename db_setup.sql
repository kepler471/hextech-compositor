CREATE TABLE summoners
/*
persons will be the reference table for summoners and account info
there may be non-static data, such as current ranks and summoner levels,
but there should be an accompanying revisionDate to give a timestamp that
is near to when the data was collected.

PUUIDs and Other IDs:
The Riot API uses three IDs for players: summoner IDs, account IDs, and
PUUIDs. Different APIs use different IDs, and you should use whichever ID
is required by the API you are using.
Summoner and account IDs are only unique per region, and PUUIDs are unique
globally.
Because the PUUID is globally unique, when a player transfers regions
their PUUID will not change. This allows you to track summoners that have
transferred regions. If a player transfers regions, their summoner and
account IDs will change.
All IDs are encrypted using encryption keys unique to each project. An ID
obtained with your dev key will not work with your production key (and
vice versa). When you refresh a key, the encrypted ID will not change.

*/
(
    summonerName  character varying(16),
    summonerId    character varying(100) primary key,
    accountId     character varying(100),
    puuid         character varying(100),
    queueType     character varying(100),
    leagueId      character varying(100),
    wins          integer,
    losses        integer,
    revisionDate  timestamp,
    tier          character varying(10),
    rank          character varying(10),
    summonerLevel integer
);
CREATE TABLE compositions
/*
 Data from match api, key information about team compositions
 */
(
    compid        serial primary key,
    gameId        integer,
    platformId    character varying(6),
    teamId        integer,
    participantId integer,
    summonerId    character varying(100),
    championId    integer,
    pick          boolean, -- t > pick, f > ban
    winner        boolean,
    role          character varying(20),
    lane          character varying(20)

);
CREATE TABLE match
/*
 match api response dump
 */
(
    gameId   integer,
    response json
);
