def get(mist_session, org_id):
    uri = f"/api/v1/orgs/{org_id}/networks" 
    resp = mist_session.mist_get(uri, org_id=org_id)
    return resp

def create(mist_session, org_id, settings):
    uri = f"/api/v1/orgs/{org_id}/networks" 
    body = settings
    resp = mist_session.mist_post(uri, org_id=org_id, body=body)
    return resp

def get_by_id(mist_session, org_id, network_id):
    uri = f"/api/v1/orgs/{org_id}/networks/{network_id}" 
    resp = mist_session.mist_get(uri, org_id=org_id)
    return resp

def update(mist_session, org_id, network_id, settings):
    uri = f"/api/v1/orgs/{org_id}/networks/{network_id}" 
    body = settings
    resp = mist_session.mist_put(uri, org_id=org_id, body=body)
    return resp

def delete(mist_session, org_id, network_id):
    uri = f"/api/v1/orgs/{org_id}/networks/{network_id}" 
    resp = mist_session.mist_delete(uri, org_id=org_id)
    return resp



