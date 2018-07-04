#!/usr/bin/env python
# "Database code" for reporting tool to report website's logs

import psycopg2


def execute_query(query):
    """
    execute_query takes an SQL query as a parameter,
    executes the query and returns the results as a list of tuples.

    args:
      query - (string) an SQL query statement to be executed.

    returns:
      A list of tuples containing the results of the query.
    """
    try:
        # get a database connection and cursor
        db = psycopg2.connect("dbname=news")
        c = db.cursor()
        # execute the query
        c.execute(query)
        # store the results
        results = c.fetchall()
        db.commit()
        # close the database connection
        db.close()
        # return the results
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def most_popular_articles():
    """Return the most popular three articles of all time."""
    query = """select articles.title, count(log.path) as views
                from articles, log
                where concat('/article/', articles.slug) = log.path
                group by articles.title
                order by views desc
                limit 3;"""
    results = execute_query(query)
    # print results
    for r in results:
        print r[0], "__", (int(r[1])), "views"


def most_popular_authors():
    """Return the most popular article authors of all time."""
    query = """select authors.name, count(log.path) as views
                from articles, authors, log
                where articles.author = authors.id
                and concat('/article/', articles.slug) = log.path
                group by authors.name
                order by views desc
                limit 4;"""
    results = execute_query(query)
    # print results
    for r in results:
        print r[0], "__", (int(r[1])), "views"


def days_of_request_errors():
    """Return days which more than 1% of requests led to errors."""
    query = """select to_char(total.day, 'FMMonth DD, YYYY'),
                round(((errors.error_requests*100.0)/total.total_requests),3)
                as perc
                from (
                 select date(time) "day",
                    count(*) as error_requests
                    from log
                    where status='404 NOT FOUND'
                    group by day
                ) as errors
                join (
                    select date(time) "day",
                        count(*) as total_requests
                        from log
                        group by day
                ) as total
                on total.day = errors.day
                where round(((errors.error_requests*1.0)
                /total.total_requests),3) >= 0.01
                order by round(((errors.error_requests*1.0)
                /total.total_requests),3) desc;"""
    results = execute_query(query)
    # print results
    for r in results:
        print r[0], "__", (float(r[1])), "%"


if __name__ == '__main__':
    # get output of reporting tool
    print("Log Analysis Results: ")
    print("\nThe most popular articles of all time are: ")
    most_popular_articles()
    print("\nThe most popular article authors of all time are: ")
    most_popular_authors()
    print("\nThe day with more than 1% of requests lead to errors is: ")
    days_of_request_errors()
