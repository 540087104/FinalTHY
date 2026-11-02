from django.shortcuts import render
import random

# 模拟 AI 诊断知识库（任务六要求"利用 AI 生成对应功能页面"）
AI_RULES = [
    {
        "keyword": "command not found",
        "cause": "命令不存在或不在 PATH 中",
        "fix": "yum install 命令名  # 安装缺失包，或检查拼写",
    },
    {
        "keyword": "permission denied",
        "cause": "权限不足",
        "fix": "sudo chmod +x 文件名  或  sudo chown user:user 文件名",
    },
    {
        "keyword": "port",
        "cause": "端口被占用或防火墙未开",
        "fix": "netstat -tlnp | grep 端口号;  systemctl stop 占用服务;  firewall-cmd --add-port=端口号/tcp --permanent && firewall-cmd --reload",
    },
    {
        "keyword": "address already in use",
        "cause": "端口已被其他进程监听",
        "fix": "lsof -i :端口号  找到PID;  kill -9 PID",
    },
    {
        "keyword": "disk",
        "cause": "磁盘空间不足",
        "fix": "df -h;  du -sh * | sort -h  找大文件清理",
    },
    {
        "keyword": "memory",
        "cause": "内存不足 OOM",
        "fix": "free -h;  top  看谁占内存大;  kill 进程  或 加 swap",
    },
    {
        "keyword": "connection refused",
        "cause": "服务未启动或端口不对",
        "fix": "systemctl start 服务名;  systemctl status 服务名;  netstat -tlnp",
    },
    {
        "keyword": "timeout",
        "cause": "网络超时 / 防火墙拦截",
        "fix": "ping 目标IP;  traceroute 目标IP;  检查防火墙规则",
    },
]


def diagnose_error(log_text):
    """模拟 AI 根因定位"""
    log_lower = log_text.lower()
    hits = [r for r in AI_RULES if r["keyword"] in log_lower]
    if hits:
        return hits[0]
    return {
        "keyword": "unknown",
        "cause": "未能匹配到已知规则，建议检查：语法拼写 / 依赖安装 / 版本兼容性 / 路径配置",
        "fix": "1) 确认命令拼写正确\n2) 运行 pip install -r requirements.txt\n3) 检查 Python/包版本\n4) 确认文件路径无误",
    }


def index(request):
    error_log = request.POST.get("error_log", "")
    result = None
    if error_log.strip():
        result = diagnose_error(error_log)
    return render(request, "index.html", {"error_log": error_log, "result": result})
