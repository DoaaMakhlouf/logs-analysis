# "Database code" for reporting tool to report website's logs

import psycopg2


def most_popular_articles():
    """Return the most popular three articles of all time."""
    # open connection
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    # run query
    c.execute("""select articles.title, count(log.path) as views
                from articles, log
                where concat('/article/', articles.slug) = log.path
                group by articles.title
                order by views desc
                limit 3;""")
    # read and save results
    results = c.fetchall()
    db.commit()
    # close connection
    db.close()
    # print results
    for r in results:
        print (r[0]), "__", (int(r[1])), "views"


def most_popular_authors():
    """Return the most popular article authors of all time."""
    # open connection
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    # run query
    c.execute("""select authors.name, count(log.path) as views
                from articles, authors, log
                where articles.author = authors.id
                and concat('/article/', articles.slug) = log.path
                group by authors.name
                order by views desc
                limit 4;""")
    # read and save results
    results = c.fetchall()
    db.commit()
    db.close()
    # print results
    for r in results:
        print (r[0]), "__", (int(r[1])), "views"


def days_of_request_errors():
    """Return days which more than 1% of requests led to errors."""
    # open connection
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    # run query
    c.execute("""select total.day,
                round(((errors.error_requests*100.0)/total.total_requests),3)
                as perc
                from (
                 select to_char(date(time),'Month DD,YYYY') "day",
                    count(*) as error_requests
                    from log
                    where status='404 NOT FOUND'
                    group by day
                ) as errors
                join (
                    select to_char(date(time),'Month DD,YYYY') "day",
                        count(*) as total_requests
                        from log
                        group by day
                ) as total
                on total.day = errors.day
                where round(((errors.error_requests*1.0)
                /total.total_requests),3) >= 0.01
                order by round(((errors.error_requests*1.0)
                /total.total_requests),3) desc;""")
    # read and save results
    results = c.fetchall()
    db.commit()
    db.close()
    # print results
    for r in results:
        print (r[0]), "__", (float(r[1])), "%"

# get output of reporting tool
print("Log Analysis Results: \n")
print("The most popular articles of all time are: ")
most_popular_articles()
print("\nThe most popular article authors of all time are: ")
most_popular_authors()
print("\nThe day with more than 1% of requests lead to errors is: ")
days_of_request_errors()
