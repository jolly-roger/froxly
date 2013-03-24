def application(env, s_res):
    s = '200 OK'
    res_headers = [('Content-type', 'text/plain')]
    s_res(s, res_headers)
    #return [str(env)]
    return ['Yo!!!']