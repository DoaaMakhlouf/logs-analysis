# "Database code" for reporting tool to report website's logs

import psycopg2


def most_popular_articles():
    """Return the most popular three articles of all time."""
    db = pyscopg2.connect(dbname="news")
    c = db.cursor()
    c.execute("""select articles.title, count(log.path) as views
                from articles, log
                where concat('/article/', articles.slug) = log.path
                group by articles.title
                order by views desc
                limit 3;""")
    results = c.fetchall()
    db.commit()
    db.close()
    return results


def most_popular_authors():
    """Return the most popular article authors of all time."""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("""select authors.name, count(log.path) as views
                from articles, authors, log
                where articles.author = authors.id
                and concat('/article/', articles.slug) = log.path
                group by authors.name
                order by views desc
                limit 4;""")
    results = c.fetchall()
    db.commit()
    db.close()
    return results


def days_of_request_errors():
    """Return days which more than 1% of requests led to errors."""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("""create view error_percentage as
                    select (cast((select count(*) from log
                    where status = '404 NOT FOUND') as Float) * 100
                    / cast(count(status) as Float)
                as error
                from log;""")
    c.execute("""create view formatted_date as
                select to_char(date(log.time), 'Month DD, YYYY')
                as date
                from log;""")
    c.execute("""select error_percentage.error, formatted_date.date
                from error_percentage join formatted_date
                where error_percentage.error >= 0.01
                group by formatted_date.date;""")
    results = c.fetchall()
    db.commit()
    db.close()
    return results
