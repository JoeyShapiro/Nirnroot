-- auto-generated definition
create table quests
(
    id          bigint auto_increment
        primary key,
    type        enum ('journal', 'quest', 'task')                                                          not null,
    title       varchar(256)                                                                               not null,
    description varchar(4096)                                                                              null,
    parent_id   bigint                                                                                     not null,
    share       bigint                                                                                     null comment 'For now, nothing, but later assign to id in share ?table',
    secret      tinyint(1)                                                       default 0                 not null,
    start_date  datetime                                                         default CURRENT_TIMESTAMP not null,
    update_date datetime                                                         default CURRENT_TIMESTAMP not null,
    due_date    datetime                                                                                   null,
    status      enum ('pending', 'accepted', 'active', 'cancelled', 'completed') default 'pending'         not null,
    `grouping`  enum ('solo', 'party', 'competitive')                            default 'solo'            null comment 'if they are solo, this does not matter',
    constraint id
        unique (id)
);

-- dummy data
INSERT INTO nirnroot.quests (id, type, title, description, parent_id, share, secret, start_date, update_date, due_date, status, `grouping`) VALUES (1, 'journal', 'Projects', 'All of the projects I plan to work on. *cough* vaporware *cough*', 0, null, 0, '2023-03-28 20:19:37', '2023-03-28 20:19:37', null, 'pending', 'solo');
INSERT INTO nirnroot.quests (id, type, title, description, parent_id, share, secret, start_date, update_date, due_date, status, `grouping`) VALUES (2, 'journal', 'Misc', null, 0, null, 0, '2023-03-28 20:19:37', '2023-03-28 20:19:37', null, 'pending', 'solo');
INSERT INTO nirnroot.quests (id, type, title, description, parent_id, share, secret, start_date, update_date, due_date, status, `grouping`) VALUES (3, 'quest', 'Nirnroot', 'this', 1, null, 0, '2023-03-28 20:19:37', '2023-03-28 20:19:37', null, 'pending', 'solo');
INSERT INTO nirnroot.quests (id, type, title, description, parent_id, share, secret, start_date, update_date, due_date, status, `grouping`) VALUES (4, 'quest', 'SColution', 'Solution file custom made for vscode', 1, null, 0, '2023-03-28 20:19:37', '2023-03-28 20:19:37', null, 'pending', 'solo');
INSERT INTO nirnroot.quests (id, type, title, description, parent_id, share, secret, start_date, update_date, due_date, status, `grouping`) VALUES (5, 'quest', 'RICE', 'Create a linux RICE finally', 1, null, 0, '2023-04-01 02:44:43', '2023-04-01 02:44:43', null, 'pending', 'solo');
INSERT INTO nirnroot.quests (id, type, title, description, parent_id, share, secret, start_date, update_date, due_date, status, `grouping`) VALUES (6, 'journal', 'Talk', 'Random stuff to talk about', 0, null, 0, '2023-04-01 02:44:43', '2023-04-01 02:44:43', null, 'pending', 'solo');
INSERT INTO nirnroot.quests (id, type, title, description, parent_id, share, secret, start_date, update_date, due_date, status, `grouping`) VALUES (7, 'quest', 'Persimmon', 'Create AI thing for anime', 1, null, 0, '2023-04-01 02:44:43', '2023-04-01 02:44:43', null, 'pending', 'solo');
INSERT INTO nirnroot.quests (id, type, title, description, parent_id, share, secret, start_date, update_date, due_date, status, `grouping`) VALUES (8, 'quest', 'Cilantro', 'Modular 3D renderer that can output to anything', 1, null, 0, '2023-04-01 02:44:43', '2023-04-01 02:44:43', null, 'pending', 'solo');
INSERT INTO nirnroot.quests (id, type, title, description, parent_id, share, secret, start_date, update_date, due_date, status, `grouping`) VALUES (9, 'task', 'update mal', null, 2, null, 0, '2023-04-01 02:44:43', '2023-04-01 02:44:43', null, 'pending', 'solo');
INSERT INTO nirnroot.quests (id, type, title, description, parent_id, share, secret, start_date, update_date, due_date, status, `grouping`) VALUES (10, 'task', 'Wait for MAL fix', null, 7, null, 0, '2023-04-01 02:45:45', '2023-04-01 02:45:45', null, 'pending', 'solo');
INSERT INTO nirnroot.quests (id, type, title, description, parent_id, share, secret, start_date, update_date, due_date, status, `grouping`) VALUES (11, 'quest', 'Server', null, 1, null, 0, '2023-04-01 02:45:45', '2023-04-01 02:45:45', null, 'pending', 'solo');
INSERT INTO nirnroot.quests (id, type, title, description, parent_id, share, secret, start_date, update_date, due_date, status, `grouping`) VALUES (12, 'task', 'Setup samba', null, 11, null, 0, '2023-04-01 02:46:20', '2023-04-01 02:46:20', null, 'pending', 'solo');
INSERT INTO nirnroot.quests (id, type, title, description, parent_id, share, secret, start_date, update_date, due_date, status, `grouping`) VALUES (13, 'task', 'rust c wrappers', null, 8, null, 0, '2023-04-01 02:48:34', '2023-04-01 02:48:34', null, 'pending', 'solo');
INSERT INTO nirnroot.quests (id, type, title, description, parent_id, share, secret, start_date, update_date, due_date, status, `grouping`) VALUES (14, 'task', 'group activities', null, 3, null, 0, '2023-04-01 02:48:34', '2023-04-01 02:48:34', null, 'pending', 'solo');
INSERT INTO nirnroot.quests (id, type, title, description, parent_id, share, secret, start_date, update_date, due_date, status, `grouping`) VALUES (15, 'task', 'add priority, should be easy', null, 3, null, 0, '2023-04-01 02:49:21', '2023-04-01 02:49:21', null, 'pending', 'solo');
