tasks = [
    {
        'url': 'https://bgithub.xyz/juv/vibranceGUI/releases',  # HTML页面
        'selector': '//*[@id="repo-content-pjax-container"]/div/div[3]/section/div/div[2]/div/div[1]',  # XPath
        'is_json': False
    },
    {
        'url': 'https://www.123pan.com/b/api/share/get?3123308819=1733541022-9884997-2440045577&limit=100&next=-1&orderBy=create_at&orderDirection=desc&shareKey=DSu8Vv-toWc3&SharePwd=iidw&ParentFileId=8066690&Page=1',  # JSON接口
        'selector': 'data/InfoList/2/FileName',  # JSON路径
        'is_json': True
    }
]
