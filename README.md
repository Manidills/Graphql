# Graphql


Simple graphql project that use GraphQLView to show how graphql query that extract the data from database.

1. Install req.txt
2. Run GAPP.py (python GAPP.py)
3. Give this query 
                    {
            allPosts{
                edges{
                node{
                    title, body
                    author{
                    username
                    }
                }
                }
            }
            }
4. Hola ! we got the datas from database.
