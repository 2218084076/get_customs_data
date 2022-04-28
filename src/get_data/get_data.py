# coding=utf-8
import json
import logging
import random
import time
from pathlib import Path
import pandas as pd
from playwright.sync_api import sync_playwright

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

result_json = []

now_time = time.strftime("%Y-%m-%d.%H.%M", time.localtime())


def read_csv(file_path: Path) -> list:
    """
    read csv file return list
    :param: csv file path
    :return: id list
    """
    logging.debug('read csv file%s:' % file_path)
    data = pd.read_csv(file_path, usecols=[0], encoding='gbk')
    id_list = []
    for n in data.values.tolist():
        if len(str(n[0])) == 8:
            id_list.append(n[0])
    logging.debug('return id list ')
    return id_list


def main_action(file_path: Path, year: str, start_month: str, end_month: str, result_json_path: Path) -> None:
    """
    browser action
    :param file_path:
    :param year:
    :param start_month:
    :param end_month:
    :param result_json_path:
    """
    playwright = sync_playwright().start()
    browser = playwright.webkit.launch(headless=False)
    page = browser.new_page()
    # Go to http://43.248.49.97/
    page.goto("http://43.248.49.97/")
    page.wait_for_timeout(2000)
    title = page.title()
    logging.debug('page title: %s' % title)
    page.wait_for_timeout(random.randint(100, 400))
    id_list = read_csv(Path(file_path))

    for key in id_list:
        logging.debug('find %s' % key)
        page.frame_locator("iframe").nth(1).locator("select[name=\"year\"]").select_option(year)
        page.frame_locator("iframe").nth(1).locator("select[name=\"year\"]").click()
        page.wait_for_timeout(random.randint(100, 200))
        # Select start month
        page.frame_locator("iframe").nth(1).locator("select[name=\"startMonth\"]").select_option(start_month)
        page.frame_locator("iframe").nth(1).locator("select[name=\"startMonth\"]").click()
        page.wait_for_timeout(random.randint(100, 200))
        # Select end month
        page.frame_locator("iframe").nth(1).locator("select[name=\"endMonth\"]").select_option(end_month)
        page.frame_locator("iframe").nth(1).locator("select[name=\"endMonth\"]").click()
        page.wait_for_timeout(random.randint(100, 200))
        # Select CODE_TS
        page.frame_locator("iframe").nth(1).locator("select[name=\"outerField1\"]").select_option("CODE_TS")
        page.frame_locator("iframe").nth(1).locator("input[name=\"outerValue1\"]").click()
        page.wait_for_timeout(100)
        # Select ORIGIN_COUNTRY
        page.frame_locator("iframe").nth(1).locator("select[name=\"outerField2\"]").select_option(
            "ORIGIN_COUNTRY")
        page.frame_locator("iframe").nth(1).locator("select[name=\"outerField2\"]").click()
        page.wait_for_timeout(100)
        # Select TRADE_MODE
        page.frame_locator("iframe").nth(1).locator("select[name=\"outerField3\"]").select_option(
            "TRADE_MODE")
        page.frame_locator("iframe").nth(1).locator("select[name=\"outerField3\"]").click()
        # Select TRADE_CO_PORT
        page.wait_for_timeout(100)
        page.frame_locator("iframe").nth(1).locator("select[name=\"outerField4\"]").select_option(
            "TRADE_CO_PORT")
        page.frame_locator("iframe").nth(1).locator("select[name=\"outerField4\"]").click()
        page.wait_for_timeout(100)
        # input keywords
        page.frame_locator("iframe").nth(1).locator("input[name=\"outerValue1\"]").fill(f"{key}")
        page.wait_for_timeout(100)
        # Click text=查询
        page.frame_locator("iframe").nth(1).locator("text=查询").click()
        page.wait_for_timeout(300)
        # Click text=确定
        page.frame_locator("iframe").nth(1).locator("text=确定").click()
        page.wait_for_timeout(200)
        page.frame_locator("iframe").nth(1).frame_locator("iframe[name=\"layui-layer-iframe2\"]").locator(
            "text=确定").click()
        page.frame_locator('iframe').nth(1).frame_locator('iframe').locator('#msg').evaluate(
            'document.getElementById("msg").value="1"')
        msg = page.frame_locator('iframe').nth(1).frame_locator('iframe').locator('#msg').evaluate(
            'document.getElementById("msg").value')
        logging.debug('msg_value: %s' % msg)
        # click 确定
        page.frame_locator('iframe').nth(1).frame_locator('iframe').locator('#doSearch').click()
        page.wait_for_timeout(100)
        page_size = page.frame_locator("iframe").nth(1).locator('.c-666').nth(0).inner_text()
        page_num = int(page_size.split('共查询到')[1].split('条数据')[0])

        if page_num > 200:
            page.frame_locator("iframe").nth(1).locator('#pageSize').select_option('200')
            page.frame_locator("iframe").nth(1).locator('#pageSize').click()
            logging.debug('page size: %s' % page_size)
            for p in range(200):
                info = page.frame_locator("iframe").nth(1).locator('#table').evaluate(r'''
get_info = function() {
  var a, i, l, result_json, result_list, _i, _len;
  a = document.getElementsByClassName("text-c  mt-10")[%s];
  l = a.getElementsByTagName("td");
  result_list = [];
  for (_i = 0, _len = l.length; _i < _len; _i++) {
    i = l[_i];
    result_list.push(i.innerText.replaceAll("\n", "").replaceAll("\t", ""));
  }
  result_json = {
    'id': result_list[0],
    'product_name': result_list[1],
    'Partner_code': result_list[2],
    'Partner name': result_list[3],
    'trade_code': result_list[4],
    'trade_name': result_list[5],
    'area_code': result_list[6],
    'location': result_list[7],
    'first_quantity': result_list[8],
    'first_unit': result_list[9],
    'second_quantity': result_list[10],
    'second_unit': result_list[11],
    'RMB': result_list[12]
  };
  return result_json;
};
                        ''' % p)
                page.wait_for_timeout(random.randint(100, 300))
                result_json.append(info)
                logging.debug("get info: %s" % info)
            page.frame_locator("iframe").nth(1).locator('.mr-10').locator('.size-S').nth(2).click()
            page.wait_for_timeout(500)
            for p in range(page_num - 200):
                info = page.frame_locator("iframe").nth(1).locator('#table').evaluate(r'''
get_info = function() {
  var a, i, l, result_json, result_list, _i, _len;
  a = document.getElementsByClassName("text-c  mt-10")[%s];
  l = a.getElementsByTagName("td");
  result_list = [];
  for (_i = 0, _len = l.length; _i < _len; _i++) {
    i = l[_i];
    result_list.push(i.innerText.replaceAll("\n", "").replaceAll("\t", ""));
  }
  result_json = {
    'id': result_list[0],
    'product_name': result_list[1],
    'Partner_code': result_list[2],
    'Partner name': result_list[3],
    'trade_code': result_list[4],
    'trade_name': result_list[5],
    'area_code': result_list[6],
    'location': result_list[7],
    'first_quantity': result_list[8],
    'first_unit': result_list[9],
    'second_quantity': result_list[10],
    'second_unit': result_list[11],
    'RMB': result_list[12]
  };
  return result_json;
};
                        ''' % p)
                page.wait_for_timeout(random.randint(100, 300))
                result_json.append(info)
                logging.debug("get info: %s" % info)

        else:
            page.frame_locator("iframe").nth(1).locator('#pageSize').select_option('200')
            page.frame_locator("iframe").nth(1).locator('#pageSize').click()
            logging.debug('page size: %s' % page_size)

            for p in range(page_num):
                info = page.frame_locator("iframe").nth(1).locator('#table').evaluate(r'''
    get_info = function() {
      var a, i, json, l, n, r_l, _i, _j, _len, _len1;
      a = document.getElementsByClassName("text-c  mt-10")[%s];
      l = a.getElementsByTagName("td");
      r_l = [];
      for (_i = 0, _len = l.length; _i < _len; _i++) {
        i = l[_i];
        r_l.push(i.innerText.replaceAll("\n", "").replaceAll("\t", ""));
        for (_j = 0, _len1 = r_l.length; _j < _len1; _j++) {
          n = r_l[_j];
          json = {
            'id': r_l[0],
            'product_name': r_l[1],
            'first_q': r_l[2],
            'first_n': r_l[3],
            'second_q': r_l[4],
            'second_n': r_l[5],
            'rmb': r_l[6]
          };
        }
      }
      return json;
    };
                ''' % p)
                result_json.append(info)
                logging.debug("get info: %s" % info)
        page.frame_locator("iframe").nth(1).locator('.btn-link').nth(0).click()
        page.wait_for_timeout(random.randint(200, 500))
        save_json(result_json, Path(result_json_path + '%s_%s_%s%s.json' % (year, start_month, end_month, now_time)))

    page.wait_for_timeout(2000)
    page.close()
    logging.debug('playwright stop')
    browser.close()


def save_json(content_json: list, result_json_path: Path):
    """
    save result data json file
    :param content_json:
    :param result_json_path:
    """
    with open(result_json_path, 'w', encoding='utf-8') as file_obj:
        listarr2 = json.dumps(content_json, ensure_ascii=False)
        file_obj.write(listarr2)

# id_list = read_csv('商品参数导出.csv')
# print(id_list)
# for d in id_list:
# main('商品参数导出.csv', '2021', '1', '3', r'D:\github\get_customs_data')
