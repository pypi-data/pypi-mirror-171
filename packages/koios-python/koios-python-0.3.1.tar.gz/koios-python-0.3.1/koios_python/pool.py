#!/usr/bin/env python
"""
Provides all pool functions
"""
import json
import requests
from .urls import POOL_BLOCKS_URL, POOL_DELEGATORS_URL, POOL_STAKE_SNAPSHOT, POOL_HISTORY_URL, \
    POOL_DELEGATORS_HISTORY_URL, POOL_INFO_URL, POOL_LIST_URL, POOL_METADATA_URL, POOL_RELAYS_URL, \
    POOL_UPDATES_URL


def get_pool_list(content_range="0-999"):
    """
    Get a list of all currently registered/retiring (not retired) pools.

    :param str range: paginated content range, up to  1000 records.
    :return: list of all registered/retiring pools.
    :rtype: list.
    """
    custom_headers = {"Range": str(content_range)}
    pool_list = requests.get(POOL_LIST_URL, headers = custom_headers, timeout=10)
    pool_list = json.loads(pool_list.content)
    return pool_list


def get_pool_info(*args):
    """
    Get current pool status and details for a specified pool.

    :param str args: pool IDs in bech32 format (pool1...)
    :return: list of pool information.
    :rtype: list.
    """
    get_format = {"_pool_bech32_ids": [args] }
    pool_list = requests.post(POOL_INFO_URL, json = get_format, timeout=10)
    pool_list  = json.loads(pool_list.content)
    return pool_list


def get_pool_stake_snapshot(pool_bech32):
    """
    Returns Mark, Set and Go stake snapshots for the selected pool, useful for leaderlog calculation

    :param str pool_bech32: Pool IDs in bech32 format (pool1...)
    :return: Array of pool stake information for 3 snapshots
    :rtype: list.
    """
    
    snapshot = requests.get(POOL_STAKE_SNAPSHOT + pool_bech32, timeout=10)
    snapshot  = json.loads(snapshot.content)
    return snapshot


def get_pool_delegators(pool_bech32):
    """
    Return information about live delegators for a given pool.

    :param str pool_bech32: pool IDs in bech32 format (pool1...).
    :param str epoch_no: epoch number to get info (current if omitted).
    :return: list of pool delegators information.
    :rtype: list.
    """
    info = requests.get(POOL_DELEGATORS_URL + pool_bech32, timeout=10)
    info = json.loads(info.content)
    return info


def get_pool_delegators_history(pool_bech32, epoch_no=None):
    """
    Return information about active delegators (incl. history) for a given pool and epoch number \
    (all epochs if not specified).

    :param str pool_bech32: pool IDs in bech32 format (pool1...).
    :param str epoch_no: epoch number to get info (current if omitted).
    :return: list of pool delegators information.
    :rtype: list.
    """
    if epoch_no is None:
        info = requests.get(POOL_DELEGATORS_HISTORY_URL + pool_bech32, timeout=10)
        info = json.loads(info.content)
    else:
        info = requests.get(POOL_DELEGATORS_HISTORY_URL + pool_bech32 + "&_epoch_no=" + str(epoch_no), timeout=10)
        info = json.loads(info.content)
    return info



def get_pool_blocks(pool_bech32, epoch_no=None):
    """
    Return information about blocks minted by a given pool for all epochs (or _epoch_no if provided)

    :param str pool_bech32: pool IDs in bech32 format (pool1...).
    :param str epoch_no: epoch number to get info (from the beginning if omitted).
    :return: list of blocks created by pool.
    :rtype: list.s
    """
    if epoch_no is None:
        info = requests.get(POOL_BLOCKS_URL + pool_bech32, timeout=10)
        info = json.loads(info.content)
    else:
        info = requests.get(POOL_BLOCKS_URL + pool_bech32 + "&_epoch_no=" + str(epoch_no), timeout=10)
        info = json.loads(info.content)
    return info


def get_pool_history(pool_bech32, epoch_no="history"):
    """
    Return information about pool stake, block and reward history in a given epoch _epoch_no \
    (or all epochs that pool existed for, in descending order if no _epoch_no was provided)

    :param str pool_bech32: pool IDs in bech32 format (pool1...).
    :param str epoch_no: epoch number to get info (from the beginning if omitted).
    :return: list of blocks created by pool.
    :rtype: list.
    """
    if epoch_no == "history":
        info = requests.get(POOL_HISTORY_URL + str(pool_bech32), timeout=10)
        info = json.loads(info.content)
    else:
        info = requests.get(POOL_HISTORY_URL + str(pool_bech32) + "&_epoch_no=" + str(epoch_no), timeout=10)
        info = json.loads(info.content)
    return info


def get_pool_updates(pool_bech32=None):
    """
    Get all pool updates for all pools or only updates for specific pool if specified.

    :param str pool_bech32: pool IDs in bech32 format (pool1...).
    :return: list of historical pool updates.
    :rtype: list.
    """
    if pool_bech32 is None:
        pool_list = requests.get(POOL_UPDATES_URL, timeout=10)
        pool_list  = json.loads(pool_list.content)
    else:
        pool_list = requests.get(POOL_UPDATES_URL + "?_pool_bech32=" + pool_bech32, timeout=10)
        pool_list  = json.loads(pool_list.content)
    return pool_list


def get_pool_relays(content_range="0-999"):
    """
    Get a list of registered relays for all currently registered/retiring (not retired) pools.

    :param str range: paginated content range, up to  1000 records.
    :return: list of pool relay information.
    :rtype: list.
    """
    custom_headers = {"Range": str(content_range)}
    pool_list = requests.get(POOL_RELAYS_URL, headers = custom_headers, timeout=10)
    pool_list  = json.loads(pool_list.content)
    return pool_list


def get_pool_metadata(*args):
    """
    Get Metadata (on & off-chain) for all currently registered/retiring (not retired) pools.

    :param str args: pool IDs in bech32 format (pool1...).
    :return: list of pool metadata.
    :rtype: list.
    """
    if len(args) == 0:
        pool_list = requests.post(POOL_METADATA_URL, timeout=10)
        pool_list  = json.loads(pool_list.content)
    else:
        get_format = {"_pool_bech32_ids": [args]}
        pool_list = requests.post(POOL_METADATA_URL, json = get_format, timeout=10)
        pool_list  = json.loads(pool_list.content)
    return pool_list
