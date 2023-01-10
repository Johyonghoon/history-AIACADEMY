create table users(
    user_email varchar(20) primary key,
    user_id varchar(20),
    password varchar(20),
    user_name varchar(20),
    phone varchar(20),
    birth varchar(20),
    address varchar(20),
    job varchar(20),
    user_interests varchar(20),
    token varchar(20)
)charset = utf8;

create table posts(
    post_id int primary key AUTO_INCREMENT,
    title varchar(100),
    content varchar(1000),
    create_at DATETIME,
    updated_at DATETIME
)charset = utf8;

# insert into users(user_email, user_id, password, user_name, phone, birth, address, job, user_interests)
# values ('hong@test.com', 'GILDONG', '1', '홍길동', '010-1234-5678', '2000-01-01', '서울시 강남구', '개발자', '영화');
#
# insert into users(user_email, user_id, password, user_name, phone, birth, address, job, user_interests)
# values ('park@test.com', 'JayPark', '1', '박재범', '010-3344-5678', '2000-07-01', '서울시 강북구', '개발자', '여행');
#
# select * from users;