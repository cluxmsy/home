from email import header
from urllib import response
import requests

#执行api调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url,headers=headers)
print(f"Status code: {r.status_code}")
#将api响应赋给一个变量
response_dict = r.json()
print(f"total respositoris：{response_dict['total_count']}")

#探索有关仓库的信息
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# #研究第一个仓库
# repo_dict = repo_dicts[0]

# print(f"\nSelected information about first repository:")
print("\nSelected information about each repository:")
#遍历每一个项目的名称、所有者、星级、url、以及其描述
for repo_dict in repo_dicts:
    print(f"Name:{repo_dict['name']}")
    print(f"Owner:{repo_dict['owner']['login']}")
    print(f"Start:{repo_dict['stargazers_count']}")
    print(f"Repository:{repo_dict['html_url']}")
    # print(f"Created:{repo_dict['created_at']}")
    # print(f"Updated:{repo_dict['updated_at']}")
    print(f"Description:{repo_dict['description']}")

# print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)

# #处理结果
# print(response_dict.keys())
