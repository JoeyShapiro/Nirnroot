-- auto-generated definition
create table quests
(
    id          bigint auto_increment
        primary key,
    type        enum ('journal', 'quest', 'task') not null,
    title       varchar(256)                      not null,
    description varchar(4096)                     null,
    parent_id   bigint                            not null,
    share       bigint                            null comment 'For now, nothing, but later assign to id in share ?table',
    secret      tinyint(1) default 0              not null,
    constraint id
        unique (id)
);

-- dummy data
INSERT INTO nirnroot.quests (id, type, title, description, parent_id, share, secret) VALUES (1, 'journal', 'Projects', 'All of the projects I plan to work on. *cough* vaporware *cough*', 0, null, 0);
INSERT INTO nirnroot.quests (id, type, title, description, parent_id, share, secret) VALUES (2, 'journal', 'Misc', null, 0, null, 0);
INSERT INTO nirnroot.quests (id, type, title, description, parent_id, share, secret) VALUES (3, 'quest', 'Nirnroot', 'this', 1, null, 0);
INSERT INTO nirnroot.quests (id, type, title, description, parent_id, share, secret) VALUES (4, 'quest', 'SColution', 'Solution file custom made for vscode', 1, null, 0);
INSERT INTO nirnroot.quests (id, type, title, description, parent_id, share, secret) VALUES (5, 'quest', 'Cilantro', 'Modular 3D renderer that can output to anything', 1, null, 0);
