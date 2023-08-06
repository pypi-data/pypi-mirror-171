#!/usr/bin/env python
"""
Provides all asset functions
"""
import json
import requests
from .urls import ASSET_ADDRESS_LIST_URL, ASSET_HISTORY_URL, ASSET_INFO_URL, ASSET_LIST_URL, \
    ASSET_POLICY_INFO_URL, ASSET_SUMMARY_URL, ASSET_TXS_URL


def get_asset_list():
    """
    Get the list of all native assets (paginated)

    :return: list with all asset list.
    :rtype: list.
    """
    list = requests.get(ASSET_LIST_URL, timeout=10)
    list = json.loads(list.content)
    return list


def get_asset_address_list(asset_policy, asset_name):
    """
    Get the list of all addresses holding a given asset.

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :param str asset_name: string with Asset Name in hexadecimal format (hex).
    :return: list of all addresses.
    :rtype: list.
    """
    info = requests.get(ASSET_ADDRESS_LIST_URL + asset_policy + "&_asset_name=" + asset_name, timeout=10)
    info = json.loads(info.content)
    return info


def get_asset_info(asset_policy, asset_name):
    """
    Get the information of an asset including first minting & token registry metadata.

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :param str asset_name: string with Asset Name in hexadecimal format (hex).
    :return: list of all asset info.
    :rtype: list.
    """
    info = requests.get(ASSET_INFO_URL + str(asset_policy) + "&_asset_name=" + str(asset_name), timeout=10)
    info = json.loads(info.content)
    return info


def get_asset_history(asset_policy, asset_name):
    """
    Get the mint/burn history of an asset.

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :param str asset_name: string with Asset Name in hexadecimal format (hex).
    :return: list of asset mint/burn history.
    :rtype: list.
    """
    history = requests.get(ASSET_HISTORY_URL + str(asset_policy) + "&_asset_name=" + str(asset_name), timeout=10)
    history = json.loads(history.content)
    return history


def get_asset_policy_info(asset_policy):
    """
    Get the information for all assets under the same policy.

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :return: list of all mint/burn transactions for an asset
    :rtype: list.
    """
    info = requests.get(ASSET_POLICY_INFO_URL + asset_policy, timeout=10)
    info = json.loads(info.content)
    return info


def get_asset_summary(asset_policy, asset_name):
    """
    Get the summary of an asset (total transactions exclude minting/total wallets include only
    wallets with asset balance).

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :param str asset_name: string with Asset Name in hexadecimal format (hex).
    :return: list of asset summary information.
    :rtype: list.
    """
    summary = requests.get(ASSET_SUMMARY_URL + asset_policy + "&_asset_name=" + asset_name, timeout=10)
    summary = json.loads(summary.content)
    return summary


def get_asset_txs(asset_policy, asset_name, after_block_height=0):
    """
    Get the list of all asset transaction hashes (newest first).

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :param str asset_name: string with Asset Name in hexadecimal format (hex).
    :param int after_block_height: Block height for specifying time delta, if not data start from 0
    :return: list of all asset hashes transactions.
    :rtype: list.
    """
    txs = requests.get(ASSET_TXS_URL + asset_policy + "&_asset_name=" + asset_name + \
        "&_after_block_height=" + str(after_block_height), timeout=10)
    txs = json.loads(txs.content)
    return txs
    