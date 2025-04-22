from abc import ABC, abstractmethod
from typing import Self, Any
from config import UI_MAX_WAIT_TIME, TIME_FORMAT, UI_SCREENSHOT_ABS_DIR


class BaseAlert(ABC):
    @abstractmethod
    def accept(self):
        """接受弹窗"""

    @abstractmethod
    def dismiss(self):
        """拒绝弹窗"""

    @abstractmethod
    def send_keys(self, text: str):
        """输入文本到弹窗"""

    def get_text(self) -> str:
        """获取弹窗文本"""


class BaseElement(ABC):
    max_wait_time = UI_MAX_WAIT_TIME

    @abstractmethod
    def click(self):
        """左键点击"""

    @abstractmethod
    def input(self, text: str):
        """输入文字"""

    @abstractmethod
    def get_text(self) -> str | None:
        """获取元素简单文本"""

    @abstractmethod
    def get_text_content(self) -> str | None:
        """获取元素原始文本"""

    @abstractmethod
    def is_visible(self) -> bool:
        """判断元素是否可见"""

    @abstractmethod
    def get_attribute(self, attribute: str) -> str | None:
        """获取元素属性"""

    @abstractmethod
    def wait_visible(self, max_wait_time: float = None) -> Self:
        """等待元素可见"""

    @abstractmethod
    def wait_enable(self, max_wait_time: float = None) -> Self:
        """等待元素启用"""

    @abstractmethod
    def wait_editable(self, max_wait_time: float = None) -> Self:
        """等待元素可编辑"""

    @abstractmethod
    def wait_clickable(self, max_wait_time: float = None) -> Self:
        """等待元素可点击"""

    @abstractmethod
    def wait_non_zreo_size(self, max_wait_time: float = None) -> Self:
        """等待元素非零尺寸"""

    @abstractmethod
    def select_by_value(self, value: str):
        """通过值选择下拉框选项"""

    @abstractmethod
    def select_by_index(self, index: int):
        """通过索引选择下拉框选项"""

    @abstractmethod
    def select_by_text(self, text: str):
        """通过文本选择下拉框选项"""

    # actions
    @abstractmethod
    def move(self):
        """移动鼠标至指定位置"""

    @abstractmethod
    def drag_to(self, target: Self):
        """左键拖动目标至指定位置"""

    @abstractmethod
    def double_click(self):
        """左键双击"""

    @abstractmethod
    def right_click(self):
        """右键点击"""

    @abstractmethod
    def click_hold(self):
        """点击并按住左键"""

    @abstractmethod
    def scroll_into_view(self) -> Self:
        """垂直方向滚动到元素可见"""


class BasePage(ABC):
    time_format = TIME_FORMAT
    screenshot_dir = UI_SCREENSHOT_ABS_DIR

    @abstractmethod
    def goto(self, url: str) -> Self:
        """访问网址"""

    @abstractmethod
    def screenshot(self, filename: str):
        """截图"""

    @abstractmethod
    def get_title(self) -> str:
        """获取当前窗口标题"""

    @abstractmethod
    def get_url(self) -> str:
        """获取当前窗口URL"""

    @abstractmethod
    def close(self):
        """关闭当前窗口"""

    @abstractmethod
    def quit(self):
        """关闭浏览器"""

    @abstractmethod
    def execute_script(self, script: Any, *args: Any) -> Any:
        """执行js脚本"""

    @abstractmethod
    def find(self, selector: str) -> BaseElement:
        """查找元素"""

    @abstractmethod
    def find_all(self, selector: str) -> list[BaseElement]:
        """查找元素列表"""

    @abstractmethod
    def actions(self, selector: str) -> BaseElement:
        """动作链"""

    @staticmethod
    @abstractmethod
    def get_clipboard_content() -> str:
        """获取剪贴板内容"""

    @abstractmethod
    def switch_to_frame(self, element: BaseElement) -> Self:
        """切换frame"""

    @abstractmethod
    def switch_to_alert(self) -> BaseAlert:
        """切换alert弹窗"""


class BaseBrowser(ABC):

    def launch(self) -> BasePage:
        """运行浏览器"""

    def close(self):
        """关闭浏览器"""

    def new_page(self) -> BasePage:
        """新建页面"""

    @abstractmethod
    def switch_to_page(self, name: str) -> BasePage:
        """切换浏览器页面"""
