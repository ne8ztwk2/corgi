from abc import ABC, abstractmethod
from typing import Literal, Self, Any
from playwright.sync_api import Locator
from config import UI_MAX_WAIT_TIME, TIME_FORMAT, UI_SCREENSHOT_ABS_DIR


class BaseElement(ABC):
    max_wait_time = UI_MAX_WAIT_TIME

    @abstractmethod
    def click(self):
        """
        左键点击
        """
        pass

    @abstractmethod
    def input(self, text: str):
        """
        输入文字
        """
        pass

    @abstractmethod
    def get_text(self) -> str | None:
        """
        获取元素简单文本
        """
        pass

    @abstractmethod
    def get_text_content(self) -> str | None:
        """
        获取元素原始文本
        """
        pass

    @abstractmethod
    def is_visible(self) -> bool:
        """
        判断元素是否可见
        """
        pass

    @abstractmethod
    def get_attribute(self, attribute: str) -> str | None:
        """
        获取元素属性
        """
        pass

    @abstractmethod
    def wait_visible(self, max_wait_time: float = None) -> Self:
        """
        等待元素可见
        """
        pass

    @abstractmethod
    def wait_enable(self, max_wait_time: float = None) -> Self:
        """
        等待元素启用
        """
        pass

    @abstractmethod
    def wait_editable(self, max_wait_time: float = None) -> Self:
        """
        等待元素可编辑
        """
        pass

    @abstractmethod
    def wait_clickable(self, max_wait_time: float = None) -> Self:
        """
        等待元素可点击
        """
        pass

    @abstractmethod
    def wait_non_zreo_size(self, max_wait_time: float = None) -> Self:
        """
        等待元素非零尺寸
        """
        pass

    @abstractmethod
    def select_by_value(self, value: str):
        """
        通过值选择下拉框选项
        """
        pass

    @abstractmethod
    def select_by_index(self, index: int):
        """
        通过索引选择下拉框选项
        """
        pass

    @abstractmethod
    def select_by_text(self, text: str):
        """
        通过文本选择下拉框选项
        """
        pass

    # actions
    @abstractmethod
    def move(self):
        """
        移动鼠标至指定位置
        """
        pass

    @abstractmethod
    def drag_to(self, target: Self):
        """
        左键拖动目标至指定位置
        """
        pass

    @abstractmethod
    def double_click(self):
        """
        左键双击
        """
        pass

    @abstractmethod
    def right_click(self):
        """
        右键点击
        """
        pass

    @abstractmethod
    def click_hold(self):
        """
        点击并按住左键
        """
        pass

    @abstractmethod
    def scroll_into_view(self) -> Self:
        """
        垂直方向滚动到元素可见
        """
        pass


class BasePage(ABC):
    time_format = TIME_FORMAT
    screenshot_dir = UI_SCREENSHOT_ABS_DIR

    @abstractmethod
    def goto(self, url: str) -> Self:
        """
        访问网址
        """
        pass

    @abstractmethod
    def screenshot(self, filename: str):
        """
        截图
        """
        pass

    @abstractmethod
    def get_title(self) -> str:
        """获取当前窗口标题"""
        pass

    @abstractmethod
    def get_url(self) -> str:
        """
        获取当前窗口URL
        """
        pass

    @abstractmethod
    def close(self):
        """
        关闭当前窗口
        """
        pass

    @abstractmethod
    def quit(self):
        """
        关闭浏览器
        """
        pass

    @abstractmethod
    def alert(self, action: Literal["accept", "dismiss"], text: str = None):
        """
        操作alert弹窗
        """
        pass

    @abstractmethod
    def get_alert_text(self) -> str:
        """
        获取alert弹窗文字
        """
        pass

    @abstractmethod
    def execute_script(self, script: Any, *args: Any) -> Any:
        """
        执行js脚本
        """
        pass

    @abstractmethod
    def find(self, selector: str) -> BaseElement:
        """
        查找元素
        """
        pass

    @abstractmethod
    def find_all(self, selector: str) -> list[BaseElement]:
        """
        查找元素列表
        """
        pass

    @abstractmethod
    def actions(self, selector: str) -> BaseElement:
        """
        动作链
        return BaseElement
        """
        pass

    @staticmethod
    @abstractmethod
    def get_clipboard_content() -> str:
        """
        获取剪贴板内容
        """
        pass

    @abstractmethod
    def switch_to_frame(self, element: BaseElement) -> Self:
        """
        切换frame
        """
        pass

    @abstractmethod
    def switch_to_window(self, name: str) -> Self:
        """
        切换浏览器窗口
        """
        pass
