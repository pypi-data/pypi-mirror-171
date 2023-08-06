# -*- coding: utf-8 -*-

from functools import partial
import hashlib
import os

import crcmod


# ----- 文件操作 -----

def remove_if_exists(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)


def get_file_size(file_path):
    """
    不存在为0，存在为file size。

    :param file_path:
    :param remove_existed:
    :return:
    """
    if os.path.exists(file_path):
        return os.path.getsize(file_path)
    else:
        return 0


# ----- 数据校验 -----

def calculate_file_md5(file_path, chunk_size=1024):
    with open(file_path, 'rb') as f:
        md5_digests = [hashlib.md5(chunk).digest() for chunk in iter(lambda: f.read(chunk_size), b'')]
    md5_str = hashlib.md5(b''.join(md5_digests)).hexdigest() + '-' + str(len(md5_digests))
    return md5_str


def calculate_file_crc64(file_path, chunk_size=None):
    """
    计算文件CRC64

    - https://cloud.tencent.com/document/product/436/40334
    - http://crcmod.sourceforge.net/crcmod.html#mkcrcfun-crc-function-factory

    :param file_path: 文件路径
    :param chunk_size: default 1024*1024
    :return:
    """
    chunk_size = chunk_size or 1024*1024
    crc64 = crcmod.Crc(0x142F0E1EBA9EA3693, initCrc=0, xorOut=0xffffffffffffffff, rev=True)
    with open(file_path, 'rb') as f:
        # https://docs.python.org/3/library/functions.html#iter
        for chunk in iter(partial(f.read, 64), b''):
            crc64.update(chunk)
    return crc64.crcValue


def verify_file_crc64(crc64_value: int, file_path: str, chunk_size=None):
    """
    校验文件CRC64

    :param crc64_value:
    :param file_path:
    :param chunk_size:
    :return:
    """
    return crc64_value == calculate_file_crc64(file_path, chunk_size)


def clean_unverified_file_crc64(crc64_value, file_path: str, chunk_size=None):
    """
    清理未校验成功的文件

    暂未使用，feature flag设计尚未明确。

    :param crc64_value:
    :param file_path:
    :param chunk_size:
    :return:
    """
    is_verified = verify_file_crc64(crc64_value=crc64_value, file_path=file_path, chunk_size=chunk_size)
    if not is_verified:
        os.remove(file_path)
    return is_verified
